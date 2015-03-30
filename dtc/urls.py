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
    url(r'^user/auth/$', v.auth_view),
    url(r'^user/loggedinUser/$', v.loggedinUser),
    url(r'^user/invalid_user/$', v.invalid_user),
    url(r'^user/invalid/$', v.invalid_user),
    url(r'^user/register/$', v.register),
    url(r'^user/register_success/$', v.register_success),

)

