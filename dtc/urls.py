from django.conf.urls import patterns, include, url
from django.contrib import admin
from twitterclone import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dtc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls))
    ,
)
