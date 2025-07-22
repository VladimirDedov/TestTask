from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_datetime

from apps_gym.users.models.trainer_profile import TrainerProfile
from apps_gym.users.models.client_profile import ClientProfile
from apps_gym.gym_room.models import GymRoom
from apps_gym.schedule.models import ScheduleModel
from apps_gym.schedule.serializers.schedule_serializers import ScheduleShortSerializer


class TrainerBookingViewSet(ViewSet):
    """
    API для записи клиентов к тренерам и просмотра записей.
    """

    def list(self, request):
        """
        GET /trainer-bookings/
        Получить все бронирования.
        """
        bookings = ScheduleModel.objects.select_related("trainer", "client", "gym")
        return Response(ScheduleShortSerializer(bookings, many=True).data)

    def create(self, request):
        """
        POST /trainer-bookings/
        Создать запись клиента к тренеру.
        """
        trainer_id = request.data.get("trainer_id")
        client_id = request.data.get("client_id")
        gym_id = request.data.get("gym_id")
        start_time = parse_datetime(request.data.get("start_time"))
        end_time = parse_datetime(request.data.get("end_time"))

        if not all([trainer_id, client_id, gym_id, start_time, end_time]):
            return Response(
                {"error": "trainer_id, client_id, gym_id, start_time, end_time обязательны"},
                status=status.HTTP_400_BAD_REQUEST
            )

        trainer = get_object_or_404(TrainerProfile, pk=trainer_id)
        client = get_object_or_404(ClientProfile, pk=client_id)
        gym = get_object_or_404(GymRoom, pk=gym_id)

        # Проверка пересечения времени
        overlap = ScheduleModel.objects.filter(
            trainer=trainer,
            start_time__lt=end_time,
            end_time__gt=start_time
        ).exists()
        if overlap:
            return Response(
                {"error": "Этот тренер уже занят в указанное время."},
                status=status.HTTP_400_BAD_REQUEST
            )

        schedule = ScheduleModel.objects.create(
            trainer=trainer,
            client=client,
            gym=gym,
            start_time=start_time,
            end_time=end_time
        )

        return Response(ScheduleShortSerializer(schedule).data, status=status.HTTP_201_CREATED)
