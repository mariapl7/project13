from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'ads', ProductViewSet)  # Эндпоинт /ads/
router.register(r'comments', CommentViewSet)  # Эндпоинт /comments/

urlpatterns = [
    path('', include(router.urls)),
]