from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Product, Comment
from .serializers import ProductSerializer, CommentSerializer
from .permissions import IsOwner, IsAdminOrReadOnly
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, CommentForm


class ProductPagination(PageNumberPagination):
    """Класс пагинации для товаров."""
    page_size = 4  # Ограничение на 4 объекта на странице


class ProductViewSet(viewsets.ModelViewSet):
    """Представление для операций с товарами."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']  # Позволяет фильтровать по имени товара

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwner()]
        elif self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAdminOrReadOnly()]
        else:
            return [permissions.AllowAny()]


class CommentViewSet(viewsets.ModelViewSet):
    """Представление для операций с комментариями."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwner()]
        elif self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAdminOrReadOnly()]
        else:
            return [permissions.AllowAny()]


# Обычные представления для работы с формами

def create_product(request):
    """Создание нового товара."""
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user  # Устанавливаем владельца товара
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'create_product.html', {'form': form})


def add_comment(request, product_id):
    """Добавление комментария к товару."""
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.owner = request.user  # Предполагается, что пользователь аутентифицирован
            comment.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form': form, 'product': product})
