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
    pass


def auth_view(request):
    pass

def auth_view(request):
    pass


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