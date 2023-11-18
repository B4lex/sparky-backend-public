import typing

from rest_framework.viewsets import ModelViewSet

from sparky.activities.api.v1.serializers import ActivitySerializer, ActivityWriteSerializer
from sparky.activities.api.v1.serializers.ongoing_activity import (
    OngoingActivitySerializer,
    OngoingActivityWriteSerializer,
)
from sparky.activities.models import Activity
from sparky.activities.selectors import ActivitySelectors, OngoingActivitySelectors
from sparky.activities.services.activity import ActivityService
from sparky.core.mixins import WriteSerializerMixin
from sparky.users.models import User


class ActivityViewSet(WriteSerializerMixin, ModelViewSet):
    serializer_class = ActivitySerializer
    write_serializer_class = ActivityWriteSerializer

    def get_queryset(self):
        return ActivitySelectors.get_available_activities_for_user(typing.cast(User, self.request.user))

    def perform_destroy(self, instance: Activity) -> None:
        ActivityService.delete(instance)


class OngoingActivityViewSet(WriteSerializerMixin, ModelViewSet):
    serializer_class = OngoingActivitySerializer
    write_serializer_class = OngoingActivityWriteSerializer

    def get_queryset(self):
        return OngoingActivitySelectors.get_ongoing_activities_for_user(typing.cast(User, self.request.user))
