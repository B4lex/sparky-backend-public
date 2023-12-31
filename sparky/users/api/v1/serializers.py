from django.contrib.auth import get_user_model
from rest_framework import serializers

from sparky.users.models import User as UserType

User = get_user_model()


class UserSerializer(serializers.ModelSerializer[UserType]):
    class Meta:
        model = User
        fields = ["id", "name"]
