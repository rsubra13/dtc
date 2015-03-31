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


    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True)
    post = models.ForeignKey(Post)
    flickrid = models.CharField(max_length=255, blank=True)

    # following fields necessary to construct the Flickr image URLs
    server = models.CharField(max_length=255, blank=True)
    farm = models.CharField(max_length=255, blank=True)
    secret = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return str(self.id)

    def construct_image_url(self):
        #return "https://farm%{farm}.staticflickr.com/%{server}/%{flickrid}_%{secret}_z.jpg" %\
        return "https://farm.staticflickr.comz.jpg" %\
        {
            'farm': self.farm,
            'server': self.server,
            'secret': self.secret,
            'flickrid': self.post.photo_id
        }







