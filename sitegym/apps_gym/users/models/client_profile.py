from django.db import models
from django.conf import settings


class ClientProfile(models.Model):
    """ Профиль клиента фитнес-зала."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,# нужна так как добавлены поля в AbstractUser
        on_delete=models.CASCADE,
        related_name="client_profile",
        verbose_name="Пользователь"
    )
    phone = models.CharField("Телефон", max_length=20, blank=True, null=True)
    trainers = models.ManyToManyField(
        "users.TrainerProfile",  # для M2M
        related_name="clients",
        verbose_name="Тренеры"
    )

    def __str__(self):
        return f"Клиент: {self.user.last_name} {self.user.first_name}"
