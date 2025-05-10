from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Пользовательская модель пользователя, наследующая от AbstractUser.

    Attributes:
        phone_number (str): Номер телефона пользователя (необязательное поле).
    """
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        """Возвращает строковое представление пользователя."""
        return self.username
