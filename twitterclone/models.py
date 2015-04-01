from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Using User class of Django instead of custom User class.


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    message = models.TextField(max_length=1024)
    created_date = models.DateTimeField()
    userId = models.ForeignKey(User)
    photo_id = models.CharField(max_length=50)
    tags = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def post_unittest(self, title):
        return "The title is "+title

    # def __init__(self, photo_id,title=None,message=None,userobj=None, tags=None):
    #     self.photo_id = photo_id
    #     self.title = title
    #     self.message = message
    #     self.created_date = dt.datetime.today()
    #     self.userId = userobj
    #     self.tags = tags





 # This model class is used to build the Flickr image URL

class Photo (models.Model):


    id = models.AutoField(primary_key=True)
    url = models.URLField(max_length=255, blank=True)
    post = models.ForeignKey(Post)


    # following fields necessary to construct the Flickr image URLs
    server = models.CharField(max_length=255, blank=True)
    farm = models.CharField(max_length=255, blank=True)
    secret = models.CharField(max_length=255, blank=True)
    flickrid = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return str(self.id)









