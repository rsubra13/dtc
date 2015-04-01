__author__ = 'Ramki Subramanian'
from django import forms
from models import Post
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'message', 'photo_id', 'tags')


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password')


class SearchForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())