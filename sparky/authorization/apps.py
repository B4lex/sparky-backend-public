from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sparky.authorization"
    verbose_name = _("Authentication")
