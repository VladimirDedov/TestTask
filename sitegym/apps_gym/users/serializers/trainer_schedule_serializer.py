from rest_framework import serializers
from apps_gym.users.models.trainer_profile import TrainerProfile
from apps_gym.users.models.client_profile import ClientProfile
from apps_gym.schedule.models import ScheduleModel
from apps_gym.gym_room.models import GymRoom

class ClientShortSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = ClientProfile
        fields = ["id", "full_name", "phone"]

    def get_full_name(self, obj):
        return f"{obj.user.last_name} {obj.user.first_name} {obj.user.middle_name or ''}".strip()

class TrainerScheduleSerializer(serializers.ModelSerializer):
    gym = serializers.CharField(source="gym.name")
    client = ClientShortSerializer()

    class Meta:
        model = ScheduleModel
        fields = ["id", "gym", "start_time", "end_time", "client"]

class GymRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymRoom
        fields = ["id", "name", "address"]

class TrainerWithScheduleSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    gyms = GymRoomSerializer(many=True)
    schedule = serializers.SerializerMethodField()

    class Meta:
        model = TrainerProfile
        fields = ["id", "full_name", "birth_date", "gender", "gyms", "schedule"]

    def get_full_name(self, obj):
        return f"{obj.user.last_name} {obj.user.first_name} {obj.user.middle_name or ''}".strip()

    def get_schedule(self, obj):
        slots = obj.schedule_slots.select_related("gym", "client__user")
        return TrainerScheduleSerializer(slots, many=True).data
