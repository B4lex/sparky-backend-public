from sparky.users.api.v1 import views
from sparky.utils.rest_framework import get_router

router = get_router()

router.register("", views.UserViewSet, "user")

urlpatterns = router.urls
