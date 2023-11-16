from sparky.authorization.selectors import GoogleOAuthSelectors
from sparky.users.models import User


class UserService:
    @staticmethod
    def get_google_api_access_token(user: User) -> str | None:
        token_instance = GoogleOAuthSelectors.get_google_social_token(user)
        return token_instance.token if token_instance else None

    @staticmethod
    def get_google_api_refresh_token(user: User) -> str | None:
        token_instance = GoogleOAuthSelectors.get_google_social_token(user)
        return token_instance.token_secret if token_instance else None
