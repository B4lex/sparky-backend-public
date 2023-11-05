from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny


@extend_schema(
    request=inline_serializer("GoogleOAuthCode", {"code": serializers.CharField()}),
    responses={status.HTTP_200_OK: inline_serializer("TokenResponse", {"key": serializers.CharField()})},
)
class GoogleOAuthLoginView(SocialLoginView):
    """
    Implements Google OAuth 2.0 authorization code flow returning the
    Auth token to authorize requests via Sparky API
    """

    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = "postmessage"
    permission_classes = [AllowAny]
