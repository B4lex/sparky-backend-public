import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response

from sparky.authorization.views import GoogleOAuthLoginView


@pytest.mark.django_db
class TestGoogleOAuthLoginView:
    @pytest.fixture
    def auth_code(self):
        return "test_auth_code"

    @pytest.fixture
    def auth_token(self):
        return "test_auth_token"

    @pytest.fixture
    def mocked_login(self, mocker):
        return mocker.patch.object(GoogleOAuthLoginView, "login")

    @pytest.fixture
    def mocked_get_response(self, mocker, auth_token):
        return mocker.patch.object(
            GoogleOAuthLoginView, "get_response", return_value=Response(data={"key": auth_token})
        )

    @pytest.fixture
    def mocked_serializer_is_valid(self, mocker):
        return mocker.patch.object(GoogleOAuthLoginView.serializer_class, "is_valid")

    def test_non_authorized_users_have_access(
        self, api_client, auth_code, auth_token, mocked_login, mocked_get_response, mocked_serializer_is_valid
    ):
        response = api_client.post(reverse("v1:auth:google"))
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"key": auth_token}
        mocked_login.assert_called_once()
        mocked_get_response.assert_called_once()
        mocked_serializer_is_valid.assert_called_once()
