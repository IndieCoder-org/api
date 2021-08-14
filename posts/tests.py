from django.test import TestCase
from .models import Post
from users.models import User


class TestPost(TestCase):

    def test_create_post(self):
        post = Post.objects.create(
            title="Django Test",
            slug="django_test",
            content="Automated testing is an extremely useful bug-killing tool for the modern Web developer.",
            up_votes=100,
            owner=User.objects.create_user(
                email="test@email.com",
                password="password1",
                nick_name="nick_name"
            )
        )
        assert post.__str__() == post.title
        assert str(post) == post.title
        assert post.slug == "django_test"
        assert post.content == str(post.content)
        assert post.up_votes == int(post.up_votes)
