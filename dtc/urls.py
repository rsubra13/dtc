from django.conf.urls import patterns, include, url
from django.contrib import admin
from twitterclone import views as v

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dtc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index', v.index),
    url(r'^login', v.login),
    url(r'^logout', v.logout),
    url(r'^user/auth/$', v.auth_view),
    url(r'^user/loggedinUser/$', v.loggedinUser),
    url(r'^user/invalid_user/$', v.invalid_user),
    url(r'^user/invalid/$', v.invalid_user),
    url(r'^user/register/$', v.register),
    url(r'^user/register_success/$', v.register_success),
    url(r'^user/new_message/$', v.new_message),
    #url(r'^user/posts/$', v.PostView.as_view()),
    url(r'^user/posts/$', v.listallposts),
    url(r'^posts/', v.listuserposts),
    url(r'^posts.json', v.listuserposts_json),
    url(r'^search/(?P<user>[a-zA-Z])/$', v.search),
    url(r'^search/$', v.search)

)

