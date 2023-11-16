from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.providers.google.provider import GoogleProvider

from sparky.users.models import User


class GoogleOAuthSelectors:
    @staticmethod
    def get_google_social_token(user: User) -> SocialToken | None:
        return user.socialaccount_set.get(provider=GoogleProvider.id).socialtoken_set.first()
