from django.db import models


class Ad(models.Model):
    """
    Модель объявления.

    Attributes:
        title (str): Заголовок объявления.
        description (str): Описание объявления.
        created_at (datetime): Дата и время создания объявления.
        updated_at (datetime): Дата и время последнего обновления объявления.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Возвращает строковое представление объявления."""
        return self.title
