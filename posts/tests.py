from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
from . models import Post

class BlogTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # create a user
        test_user1 = User.objects.create_user(username='admin', password='praise002')
        test_user1.save()
        print(test_user1)
        
        # create a blog post
        test_post = Post.objects.create(author=test_user1, title='What is python?', body='body1')
        test_post.save()
        
    def test_blog_content(self):
        post = Post.objects.first()
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'What is python?')
        self.assertEqual(body, 'body1')

# TODO: come back to it. Test failed