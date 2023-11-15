from rest_framework.viewsets import ModelViewSet

from sparky.activities.api.v1.serializers import ActivityReadSerializer, ActivityWriteSerializer
from sparky.activities.models import Activity
from sparky.activities.selectors.activity import ActivitySelectors
from sparky.activities.services.activity import ActivityService


class ActivityViewSet(ModelViewSet):
    serializer_class = ActivityReadSerializer
    queryset = ActivitySelectors.get_existing_activities()

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return ActivityWriteSerializer
        return super().get_serializer_class()

    def perform_destroy(self, instance: Activity) -> None:
        ActivityService.delete(instance)
