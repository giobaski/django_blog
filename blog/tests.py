from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

# Create your tests here.
class PostModelTest(TestCase):

    def setUp(self):
        user = User(username="testgeorge")
        user.save()
        Post.objects.create(title='testcase1', content="this is test content", author = user)

    def test_title_content(self):
        post = Post.objects.get(id=5)
        expected_object_name = f'{post.title}'
        self.assertEqual(expected_object_name, 'testcase1')


