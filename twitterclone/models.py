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






