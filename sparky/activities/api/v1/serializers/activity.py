from rest_framework import serializers

from sparky.activities.models import Activity, ActivityCategory


class ActivityCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCategory
        fields = ["id", "name"]


class ActivityWriteSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Activity
        fields = [
            "title",
            "description",
            "weight",
            "category",
            "duration",
            "start_time",
            "end_time",
            "owner",
        ]


class ActivitySerializer(serializers.ModelSerializer):
    category = ActivityCategorySerializer()

    class Meta:
        model = Activity
        fields = [
            "id",
            "title",
            "description",
            "weight",
            "category",
            "duration",
            "start_time",
            "end_time",
        ]
