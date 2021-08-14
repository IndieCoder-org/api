from django.core.files.base import ContentFile
import factory
import factory.fuzzy

from .models import Post
from users.factories import UserFactory


class PostFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Post

    title = factory.fuzzy.FuzzyText(length=50)
    content = factory.fuzzy.FuzzyText(length=300)
    up_votes = factory.fuzzy.FuzzyInteger(10, 40)
    owner = factory.SubFactory(UserFactory)
    image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data(
                {'width': 800, 'height': 450}
            ), 'example.png'
        )
    )