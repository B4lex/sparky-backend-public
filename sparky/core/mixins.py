from rest_framework.serializers import Serializer


class WriteSerializerMixin:
    serializer_class: Serializer | None = None
    write_serializer_class: Serializer | None = None
    action: str

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return self.write_serializer_class
        return self.serializer_class
