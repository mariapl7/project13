from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Административный интерфейс для пользовательской модели пользователя.

    Используется для управления пользователями через админку Django.
    """
    # Поля, отображаемые в списке
    list_display = ('username', 'email', 'phone_number', 'is_staff')
