from django.test import TestCase
from apps.blog.models import Post, Category
from django.contrib.auth.admin import User
from django.shortcuts import reverse

class BlogTests(TestCase):

    def setUp(self):
        self.author = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(title="Technology", description='none')
        self.post = Post.objects.create(
            title="Test Post",
            description="Test Description",
            text="Full text of the post",
            category=self.category,
            author=self.author)

    def test_post_creation(self):
        post = self.post
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.status, "published")  # Default value for status
        self.assertEqual(post.author, self.author)

    def test_get_absolute_url(self):
        post = self.post
        expected_url = reverse('post_detail', kwargs={'slug': post.slug})
        self.assertEqual(post.get_absolute_url(), expected_url)
