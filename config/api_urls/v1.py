from django.urls import include, path

app_name = "v1"
urlpatterns = [
    path("auth/", include("sparky.authorization.urls")),
    path("users/", include("sparky.users.api.v1.urls")),
    path("activities/", include("sparky.activities.api.v1.urls")),
]
