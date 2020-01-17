from typing import Any, Sequence

from django.contrib.auth import get_user_model
from factory import DjangoModelFactory, Faker, post_generation, SubFactory, LazyAttribute

from butter_exercise.users.models import Agreement


class UserFactory(DjangoModelFactory):

    username = Faker("user_name")
    email = Faker("email")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    name = LazyAttribute(lambda o: f"{o.first_name} {o.last_name}")

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = Faker(
            "password",
            length=42,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ).generate(extra_kwargs={})
        self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]


def generate_fake_data(object_):
    return dict(
        first_name=object_.user.first_name,
        last_name=object_.user.last_name,
        street=Faker("street_address").generate(),
        post_code=Faker("postalcode").generate(),

    )


class AgreementFactory(DjangoModelFactory):
    user = SubFactory(UserFactory)
    date = Faker("date_object")
    data = LazyAttribute(generate_fake_data)

    class Meta:
        model = Agreement
