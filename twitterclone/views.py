from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import RegistrationForm, LoginForm, PostForm, SearchForm
from models import User, Post , Photo
from django.views.generic import  ListView
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime as dt
from dtc.settings import FLICKR_API_KEY, FLICKR_SECRET, FLICKR_API_SIG , FLICKR_AUTH_TOKEN
import json, urllib2
import flickrapi # old one
import flickr_api # new
from flickr_api.api import flickr, reflection
from collections import  defaultdict
from rest_framework import serializers, parsers
from django.core.serializers.json import DjangoJSONEncoder

import datetime
import decimal
from django.db.models.base import ModelState
# Index page

def index(request):
    form = RegistrationForm()
    searchform = SearchForm()
    return render_to_response('index.html',
                            {'form': form,
                             'searchform':searchform}
                            )



def search(request, user=None):

    form = RegistrationForm()
    searchform = SearchForm()

    if request.method == "POST":
        username = request.POST.get('username', '')
        print "username" , username
        if username is not None:
            try:
                userobj = User.objects.get(username=username)
                request.session['search_user_username'] = userobj.username
                return HttpResponseRedirect('/posts/')
            except:
                userobj = None
                searcherror = " The user doesnot exist. Please try other user."
                return render_to_response('index.html',
                            {'form': form,
                             'searchform':searchform,
                             'searcherror' : searcherror}
                            )


    else:
        return render_to_response('index.html',
                            {'form': form,
                             'searchform':searchform}
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

@login_required()
def loggedinUser(request):
    return render_to_response('loggedinuser_home.html',
                              {'full_name': request.user.username})

def invalid_user(request):
     return render_to_response('loginfailed.html')


def register(request):
    searchform = SearchForm(request.POST)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'],
                                            form.cleaned_data['email'],
                                            form.cleaned_data['password'])
            user.save()
            return render_to_response('index.html',
                            {'form': form,
                             'searchform': searchform,
                             'msg' : "Registered Successfully"}
                            )

        else:
            return render_to_response('index.html',
                            {'form': form,
                             'searchform':searchform}
            )

    else:
        form = RegistrationForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    args['searchform'] = searchform
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


def logout(request):
    auth.logout(request)
    form = RegistrationForm()
    searchform = SearchForm()
    return render_to_response('index.html',
        {
            'logoutmsg' : "Logged out successfully",
            'form' : form,
            'searchform':searchform

        })


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

@login_required()
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
        main_dict[i+1].update(sub_dict)

        sub_dict.clear()

    posts = allposts
    return render_to_response('listposts.html',
                              {"posts": posts,
                              "main_dict": dict(main_dict)}
                              )




# List posts of a user ( search)

def listuserposts(request):

    search_user_name = request.session['search_user_username']


    userobj = User.objects.get(username=search_user_name)
    allposts = Post.objects.filter(userId=userobj)
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
        main_dict[i+1].update(sub_dict)
        sub_dict.clear()
        other_dict = json.dumps(main_dict, cls=DjangoJSONEncoder,sort_keys=True, indent=2)
        request.session['other_dict'] = other_dict
        request.session['search_user_name'] = search_user_name


    return render_to_response('listuserposts.html',
                              {"user": search_user_name,
                              "main_dict": dict(main_dict)}
                              )

def listuserposts_json(request):

    other_dict = request.session['other_dict']
    user = request.session['search_user_name']
    print "came here in json", other_dict

    #return HttpResponseRedirect(other_dict, mimetype="application/json")
    return render_to_response('listuserpostsjson.html',
                              {
                              "json_dict": other_dict,
                               "user": user,
                              'mimetype':'application/json'}

                              )


