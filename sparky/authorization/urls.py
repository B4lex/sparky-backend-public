from dj_rest_auth.views import LogoutView
from django.urls import path

from sparky.authorization import views

app_name = "auth"

urlpatterns = [
    path("google/", views.GoogleOAuthLoginView.as_view(), name="google"),
    path("logout/", LogoutView.as_view(), name="logout")
]
