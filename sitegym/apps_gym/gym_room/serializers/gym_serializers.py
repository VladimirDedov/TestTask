from rest_framework import serializers
from ..models import GymRoom


class GymRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymRoom
        fields = ["id", "name", "address", "capacity", "phone"]