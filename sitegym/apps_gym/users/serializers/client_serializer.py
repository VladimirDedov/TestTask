from rest_framework import serializers
from apps_gym.users.models.client_profile import ClientProfile
from apps_gym.schedule.models import ScheduleModel

class ClientScheduleSerializer(serializers.ModelSerializer):
    trainer = serializers.CharField(source="trainer.user.last_name")
    gym = serializers.CharField(source="gym.name")

    class Meta:
        model = ScheduleModel
        fields = ["id", "trainer", "gym", "start_time", "end_time"]

class ClientProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    schedule = serializers.SerializerMethodField()

    class Meta:
        model = ClientProfile
        fields = ["id", "full_name", "phone", "schedule"]

    def get_full_name(self, obj):
        return f"{obj.user.last_name} {obj.user.first_name} {obj.user.middle_name or ''}".strip()

    def get_schedule(self, obj):
        bookings = ScheduleModel.objects.filter(client=obj).select_related("trainer__user", "gym")
        return ClientScheduleSerializer(bookings, many=True).data
