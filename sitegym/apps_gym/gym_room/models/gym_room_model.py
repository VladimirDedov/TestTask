from django.db import models


class GymRoom(models.Model):
    """Модель описания зала для занятий в фитнес клубе
        Атрибуты:
        name (str): Название зала.
        address (str): Адрес зала.
        capacity (int): Максимальная вместимость.
        phone (str): Контактный телефон (необязательное поле)"""

    name = models.CharField("Название зала", max_length=100)
    address = models.CharField("Адрес", max_length=255)
    capacity = models.PositiveIntegerField("Вместимость", default=0)
    phone = models.CharField("Телефон", max_length=20, blank=True, null=True)


    def __str__(self):
        return f"{self.name} ({self.address})"
