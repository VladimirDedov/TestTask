from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from apps_gym.users.models.trainer_profile import TrainerProfile
from apps_gym.users.serializers.trainer_profile_serializer import TrainerProfileSerializer
from apps_gym.users.serializers.trainer_schedule_serializer import TrainerWithScheduleSerializer


class TrainerProfileViewSet(ModelViewSet):
    queryset = TrainerProfile.objects.select_related("user").prefetch_related("gyms")
    serializer_class = TrainerProfileSerializer

    @action(detail=True, methods=["get"])
    def schedule(self, request, pk=None):
        trainer = self.get_object()
        return Response(TrainerWithScheduleSerializer(trainer).data)
