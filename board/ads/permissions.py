from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Разрешение, позволяющее редактировать или удалять только свои объекты."""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user  # Предполагается, что у вас есть поле owner в модели


class IsAdminOrReadOnly(permissions.BasePermission):
    """Разрешение для администраторов на редактирование/удаление,
    а для остальных пользователей только на чтение."""

    def has_permission(self, request, view):
        # Разрешить доступ на чтение всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешить доступ на запись только администраторам
        return request.user and request.user.is_staff
