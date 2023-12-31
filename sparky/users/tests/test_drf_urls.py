from django.urls import resolve, reverse

from sparky.users.models import User


def test_user_detail(user: User):
    assert reverse("v1:user-detail", kwargs={"pk": user.pk}) == f"/api/v1/users/{user.pk}/"
    assert resolve(f"/api/v1/users/{user.pk}/").view_name == "v1:user-detail"


def test_user_list():
    assert reverse("v1:user-list") == "/api/v1/users/"
    assert resolve("/api/v1/users/").view_name == "v1:user-list"


def test_user_me():
    assert reverse("v1:user-me") == "/api/v1/users/me/"
    assert resolve("/api/v1/users/me/").view_name == "v1:user-me"
