from django.urls import path

from autoplanner.authorization import views

app_name = "auth"

urlpatterns = [path("google/", views.GoogleOAuthLoginView.as_view(), name="google")]
