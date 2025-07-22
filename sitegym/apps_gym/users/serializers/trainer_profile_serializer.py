from rest_framework import serializers
from apps_gym.users.models.trainer_profile import TrainerProfile
from apps_gym.gym_room.models import GymRoom
from apps_gym.users.models import User
from apps_gym.users.models.client_profile import ClientProfile


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "last_name", "first_name", "middle_name", "email"]


class GymRoomShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymRoom
        fields = ["id", "name", "address"]


# class ClientShortSerializer(serializers.ModelSerializer):
#     full_name = serializers.SerializerMethodField()
#
#     class Meta:
#         model = ClientProfile
#         fields = ["id", "full_name", "phone"]
#
#     def get_full_name(self, obj):
#         return f"{obj.user.last_name} {obj.user.first_name} {obj.user.middle_name or ''}".strip()
#
#
#
# class TrainerProfileSerializer(serializers.ModelSerializer):
#     user = UserShortSerializer(read_only=True)  # вложенный пользователь
#     gyms = GymRoomShortSerializer(many=True, read_only=True)
#     clients = ClientShortSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = TrainerProfile
#         fields = [
#             "id", "user", "gender", "gyms", "clients"
#         ]

class GymRoomShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymRoom
        fields = ["id", "name", "address"]


class TrainerProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    gyms = GymRoomShortSerializer(many=True)  # вложенный список залов

    class Meta:
        model = TrainerProfile
        fields = ["id", "full_name", "birth_date", "gender", "gyms"]

    def get_full_name(self, obj):
        return f"{obj.user.last_name} {obj.user.first_name} {obj.user.middle_name or ''}".strip()
