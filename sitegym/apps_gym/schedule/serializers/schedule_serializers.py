from rest_framework import serializers
from ..models import ScheduleModel
from apps_gym.users.serializers.client_serializer import ClientProfileSerializer


class ScheduleShortSerializer(serializers.ModelSerializer):
    client = ClientProfileSerializer()
    gym = serializers.CharField(source="gym.name")

    class Meta:
        model = ScheduleModel
        fields = ["id", "gym", "client", "start_time", "end_time"]
