from sparky.activities.api.v1 import views
from sparky.utils.rest_framework import get_router

router = get_router()

router.register("", views.ActivityViewSet, "activity")
router.register("ongoing", views.OngoingActivityViewSet, "ongoing-activity")

urlpatterns = router.urls
