from django.test import TestCase
from .models import Post
from users.models import User


class PostModelTestCase(TestCase):
    def setUp(self):
        owner = User.objects.create_superuser(
            email='admin@indiecoder.com',
            password='admin'
        )
        self.post = Post.objects.create(
            title='Test title',
            content='Test content',
            owner=owner
        )

    def test_str_representation(self):
        self.assertEqual(self.post.__str__(), self.post.title)

    def test_auto_populated_updated_at(self):
        self.assertIsNotNone(self.post.updated_at)

        old_post_updated_at = self.post.updated_at
        self.post.content = 'New test content'
        self.post.save()
        self.post.refresh_from_db()
        self.assertTrue(self.post.updated_at > old_post_updated_at)

    def test_get_absolute_url(self):
        expected_url = f'/{self.post.pk}/{self.post.slug}/'
        self.assertEqual(self.post.get_absolute_url(), expected_url)

    def test_up_votes(self):
        self.post.up_votes += 1
        self.assertEqual(self.post.up_votes, 1)
        self.post.up_votes += 1
        self.assertEqual(self.post.up_votes, 2)