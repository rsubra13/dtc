from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import RegistrationForm, LoginForm, PostForm
from models import User

from django.template import RequestContext

# Index page

def index(request):
    return render_to_response('index.html')


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
            return HttpResponseRedirect('/user/register_success'
                                        )

    else:
        form = RegistrationForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    print "comes till here", form
    return render_to_response('register.html', args)

# Succesfully registered
def register_success(request):
    message = "Registered Successfully"
    return HttpResponseRedirect('/user/register_success',
                                )
    # return render_to_response('register.html',
    #                           msg=msg)