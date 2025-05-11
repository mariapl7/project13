from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError

class Product(models.Model):
    """Модель товара."""

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def clean(self):
        if self.price < 0:
            raise ValidationError('Цена не может быть отрицательной.')

class Comment(models.Model):
    """Модель комментария."""

    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.owner} on {self.product}'
