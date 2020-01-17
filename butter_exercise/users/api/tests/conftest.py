import pytest
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from butter_exercise.users.tests.factories import AgreementFactory, UserFactory


@pytest.fixture()
def user():
    return UserFactory()


@pytest.fixture()
def api_client(user):
    client = APIClient()
    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return client


@pytest.fixture()
def agreement():
    return AgreementFactory()
