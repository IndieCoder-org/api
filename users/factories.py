from .models import User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    nick_name = factory.Faker('first_name')

