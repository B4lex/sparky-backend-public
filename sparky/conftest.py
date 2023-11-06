import pytest
from rest_framework.test import APIClient

from sparky.users.models import User
from sparky.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()
