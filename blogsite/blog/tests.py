from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class BlogTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.post = Post.objects.create(
            title='Test Title',
            slug='test-title',
            content='Hello World!',
            author = self.user,
        )
    
    def test_post_content(self):
        self.assertEqual(self.post.title, 'Test Title')
        self.assertEqual(self.post.slug, 'test-title')
        self.assertEqual(self.post.content, 'Hello World!')
        self.assertEqual(self.post.author.username, 'testuser')

    def test_post_does_not_exist(self):
        with self.assertRaises(Post.DoesNotExist) as cm:
            Post.objects.get(title='Inexistant Title')

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_status(self):
        self.assertEqual(self.post.status, 'draft')
        self.post.status = 'published'
        self.assertNotEqual(self.post.status, 'draft')
