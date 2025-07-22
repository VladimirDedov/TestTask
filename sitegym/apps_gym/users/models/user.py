from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Описание всех юзеров фитнес зала, тренеров, админов, клиентов"""
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('trainer', 'Trainer'),
        ('client', 'Client'),
    ]

    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    middle_name = models.CharField("Отчество", max_length=50, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    username = None  # delete username from AbstractUser
    email = models.EmailField("Email", unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.last_name} {self.first_name} - ({self.role})"
