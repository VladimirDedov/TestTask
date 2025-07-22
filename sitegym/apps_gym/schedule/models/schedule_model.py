from django.db import models


class ScheduleModel(models.Model):
    """Модель для описания слотов расписания тренеров.

        Атрибуты:
        trainer (TrainerProfile): Тренер, ведущий занятие.
        gym (GymRoom): Зал, в котором проходит занятие.
        start_time (datetime): Время начала занятия.
        end_time (datetime): Время окончания занятия.
        client (ClientProfile): Клиент, записанный на занятие (может быть NULL)."""

    trainer = models.ForeignKey(
        "users.TrainerProfile",
        on_delete=models.CASCADE,
        related_name="schedule_slots",
        verbose_name="Тренер"
    )
    gym = models.ForeignKey(
        "gym_room.GymRoom",
        on_delete=models.CASCADE,
        related_name="schedule_slots",
        verbose_name="Зал"
    )
    start_time = models.DateTimeField("Начало занятия")
    end_time = models.DateTimeField("Окончание занятия")
    client = models.ForeignKey(
        "users.ClientProfile",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="bookings",
        verbose_name="Клиент"
    )


    def __str__(self):
        client_name = self.client.user.last_name if self.client else "—"
        return f"{self.trainer} | {self.start_time} - {self.end_time} - ({client_name})"
