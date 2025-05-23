from django.urls import path
from .views import ResetPasswordView, ResetPasswordConfirmView, RegisterUserView


urlpatterns = [
    path('user_create', RegisterUserView.as_view(), name='user_create'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    path('reset_password_confirm/', ResetPasswordConfirmView.as_view(), name='reset_password_confirm'),
]