from django.contrib import admin
from .models import Product, Comment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Административный интерфейс для модели товара.

    Используется для управления товарами через админку Django.
    """

    list_display = ('name', 'price', 'owner', 'created_at')  # Поля, отображаемые в списке
    list_filter = ('owner',)  # Фильтрация по владельцу
    search_fields = ('name', 'description')  # Поиск по названию и описанию
    ordering = ('-price',)  # Сортировка по цене (по убыванию)

    def get_queryset(self, request):
        """Переопределяем метод для добавления дополнительной информации в список."""
        queryset = super().get_queryset(request)
        return queryset.select_related('owner')  # Оптимизация запросов с использованием связи с владельцем


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Административный интерфейс для модели комментария.

    Используется для управления комментариями через админку Django.
    """

    list_display = ('product', 'owner', 'text', 'created_at')  # Поля, отображаемые в списке
    list_filter = ('product', 'owner')  # Фильтрация по продукту и владельцу
    search_fields = ('text',)  # Поиск по тексту комментария
    ordering = ('-created_at',)  # Сортировка по дате создания (по убыванию)

    def get_queryset(self, request):
        """Переопределяем метод для добавления дополнительной информации в список."""
        queryset = super().get_queryset(request)
        return queryset.select_related('owner', 'product')  # Оптимизация запросов с использованием связей
