from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import RegistrationForm, LoginForm, PostForm
from models import User, Post , Photo
from django.views.generic import CreateView , FormView , ListView
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime as dt
from dtc.settings import FLICKR_API_KEY, FLICKR_SECRET, FLICKR_API_SIG , FLICKR_AUTH_TOKEN
import json, urllib2
import flickrapi # old one
import flickr_api # new
from flickr_api.api import flickr, reflection
from collections import  defaultdict

# Index page






def index(request):
    form = RegistrationForm()
    return render_to_response('index.html',
                            {'form': form}
                            )


def login(request):
    # Add the CSRF Token to the template context
    #c = {}
    #c.update(csrf(request))

    form = LoginForm()
    # Set the Flickr keys only once
    flickr_api.set_keys(api_key = FLICKR_API_KEY, api_secret = FLICKR_SECRET)
    return render_to_response('login.html',
                                 {'form': form,
                                    })
    #return render_to_response('login.html',
    #                          'c':c,
    #                          'form'=form)


def auth_view(request):
    """
    Uses the Django Auth Module to authenticate.
    """
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    if request.method == "POST":
        form = LoginForm(request.POST)
    # Authenticate the user and password using Django auth module
    user = auth.authenticate(username=username,
                             password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/user/loggedinUser/')
    else:
        return HttpResponseRedirect('/user/invalid_user/')


def loggedinUser(request):
    return render_to_response('loggedinuser_home.html',
                              {'full_name': request.user.username})

def invalid_user(request):
     return render_to_response('loginfailed.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'],
                                            form.cleaned_data['email'],
                                            form.cleaned_data['password'])
            user.save()
            return render_to_response('index.html',
                            {'form': form,'msg' : "Registered Successfully"}
                            )

        else:
            return render_to_response('index.html',
                            {'form': form}
            )

    else:
        form = RegistrationForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    print "comes till here", form
    return render_to_response('index.html', args)

# Succesfully registered
def register_success(request):
    message = "Registered Successfully"
    #return HttpResponseRedirect('/user/register_success',
    #                            )
    return render_to_response('index.html',
                              {'msg':message}
                            )
@login_required
def new_message(request):
    if request.method == 'POST':
       form = PostForm(request.POST)
       if form.is_valid():

           # Get the user object instance ( Foreign Key in Post Table)
           userobj = User.objects.get(id=request.user.id)

           #Add the remaining fields.
           postobj = form.save(commit=False)
           postobj.userId = userobj
           postobj.created_date = dt.datetime.today()
           postobj.save()
           flickrid = form.cleaned_data['photo_id']
           print "flickr id", flickrid

           # Try to get the flickr image url here itself

           flickr_api.set_keys(api_key = FLICKR_API_KEY, api_secret = FLICKR_SECRET) # optimize this
           flickr_response_json= flickr_api.method_call.call_api(method = "flickr.photos.getInfo", photo_id=flickrid)

           # Get these fields to construct the URL
           farm = flickr_response_json ['photo'] ['farm']
           server = flickr_response_json ['photo'] ['server']
           secret = flickr_response_json ['photo'] ['secret']


           # Construct the URL
           url = "https://farm"+str(farm)+".staticflickr.com/"+str(server)+"/"+str(flickrid)+"_"+str(secret)+"_m.jpg"

           ph = Photo(post= postobj,
                 farm = farm,
                 secret = secret,
                 server = server,
                 flickrid = flickrid,
                 url = url
                 )

           ph.save()

           return render_to_response('newpost.html',
                            {'form': form,
                             'msg' : "Message Posted Successfully",
                            'url' : url}
                            )
       else:
            return render_to_response('newpost.html',
                            {'form': form,
                             'msg' : "Please check the fields correctly"}
                            )
    else:
        form = PostForm(request.POST)
        print "comes in else of new message"
        return render_to_response('newpost.html',
                            {'form': form}
                            )
# Just for checking
class PostView(ListView):
    template_name = 'listallposts.html'
    model = Post

def listallposts(request):

    allposts = Post.objects.filter(userId=request.user.id)
    main_dict = defaultdict(dict)
    sub_dict = {}
    for i, each_post in enumerate(allposts):

        ph = Photo.objects.get(post=each_post)
        # construct the sub-dict
        sub_dict['title'] = each_post.title
        sub_dict['message'] = each_post.message
        sub_dict['created_date'] = each_post.created_date
        sub_dict['tags'] = each_post.tags
        sub_dict['url'] = ph.url

        # construct the main dict
        main_dict[i].update(sub_dict)

        sub_dict.clear()

    print " main dict", main_dict
    sample_Dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
    posts = allposts
    return render_to_response('listposts.html',
                              {"posts": posts,
                              "main_dict": dict(main_dict)}
                              )


