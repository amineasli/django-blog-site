from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Post
from .views import index, detail

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        cls.post = Post.objects.create(
            title='Test Title',
            slug='test-title',
            content='Hello World!',
            author=cls.user,
            publish='2021-04-22 16:13:01.005166+00:00',
            status='published'                                                                                                                                                                                                                                                                                                                                                                                
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
        self.assertEqual(self.post.status, 'published')
        self.post.status = 'draft'
        self.assertNotEqual(self.post.status, 'published')

    def test_post_index_view(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post List')
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_post_detail_view(self):
        response = self.client.get('/2021/04/22/test-title/')
        no_response = self.client.get('/2000/01/01/test-title/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(no_response.status_code, 400)
        self.assertTemplateUsed(response, 'blog/detail.html')
       