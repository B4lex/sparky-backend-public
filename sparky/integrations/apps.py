from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sparky.integrations"
    verbose_name = _("Integrations")
