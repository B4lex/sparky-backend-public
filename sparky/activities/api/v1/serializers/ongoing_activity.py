from rest_framework import serializers

from sparky.activities.api.v1.serializers import ActivitySerializer
from sparky.activities.models import OngoingActivity


class OngoingActivityWriteSerializer(serializers.ModelSerializer):
    activity = ActivitySerializer()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = OngoingActivity
        fields = [
            "id",
            "activity",
            "user",
        ]


class OngoingActivitySerializer(OngoingActivityWriteSerializer):
    activity = ActivitySerializer()
