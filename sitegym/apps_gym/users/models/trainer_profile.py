from django.db import models
from sitegym import settings


class TrainerProfile(models.Model):
    """Профиль тренера фитнесс зала"""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # becous changed user model with castome fields
        on_delete=models.CASCADE,
        related_name="trainer_profile",
        verbose_name="Пользователь"
    )
    birth_date = models.DateField("Дата рождения")
    gender = models.CharField(
        "Пол",
        max_length=10,
        choices=[("male", "Мужской"), ("female", "Женский")]
    )
    gyms = models.ManyToManyField(
        "gym_room.GymRoom",
        related_name="trainers",
        verbose_name="Залы"
    )

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"
