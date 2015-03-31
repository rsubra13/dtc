from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import RegistrationForm, LoginForm, PostForm
from models import User, Post , Photo
from django.views.generic import CreateView , FormView , ListView
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

def new_message(request):
    if request.method == 'POST':
       form = PostForm(request.POST)
       if form.is_valid():
           print 'yes it comes here' , form
           Post.objects.create()

       else:
           print "in else"
    else:
        form = PostForm(request.POST)
        print "comes in else of new message"
        return render_to_response('newpost.html',
                            {'form': form}
                            )




class PostView(ListView):
    template_name = 'listallposts.html'
    model = Post

def listallposts(request):
    #allposts = Post.objects.get(userId=3)
    allposts = Post.objects.all()
    #Photo.objects.get()

    paginator = Paginator(allposts,10)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Provide the default first page
        posts = paginator.page(1)
    except EmptyPage:
        # Page out of range, deliver the last page
        posts = paginator.page(paginator.num_pages)
    return render_to_response('listposts.html', {"posts": posts})

