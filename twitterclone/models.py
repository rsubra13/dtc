from django.db import models
from django.contrib.auth.models import User

# Using User class of Django instead of custom User class.


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    message = models.CharField(max_length=1024)
    created_date = models.DateTimeField()
    userId = models.ForeignKey(User)
    photo_id = models.CharField(max_length=50, unique=True)
    tags = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def post_unittest(self, title):
        return "The title is "+title


 # This model class is used to build the Flickr image URL

class Photo (models.Model):

    flickrid = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    postid = models.ForeignKey(Post)
    userid = models.ForeignKey(User)

    # following fields necessary to construct the Flickr image URLs
    server = models.CharField(max_length=255, blank=True)
    farm = models.CharField(max_length=255, blank=True)
    secret = models.CharField(max_length=255, blank=True)

    def __unicode__ (self):
        return str(self.flickrid)

    def image_url(self, code="t"):

        return "https://farm%{farm}.staticflickr.com/%{server}/%{flickrid}s_%{secret}_z.jpg" % {
            'farm': self.farm,
            'server': self.server,
            'secret': self.secret,
            'id': self.flickrid,
            'code': code
        }







