from django.test import TestCase
from twitterclone.models import Post


class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title="Post1", message=" Hi This is my first message", user_id=1, photo_id="2908978")
        Post.objects.create(title="Post2", message=" Hi This is my Second message", user_id=1, photo_id="292448978")

    def check_title(self):
        post1_obj = Post.objects.get(titl="Post1")
        post2_obj = Post.objects.get(titl="Post2")
        self.assertEqual(post1_obj.post_unittest(), 'The title is Post1')
        self.assertEqual(post2_obj.post_unittest(), 'The title is Post2')


