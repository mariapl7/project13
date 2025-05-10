from django.contrib import admin
from .models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """
    Административный интерфейс для модели объявления.

    Используется для управления объявлениями через админку Django.
    """

    list_display = ('title', 'created_at', 'updated_at')  # Поля, отображаемые в списке
