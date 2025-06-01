from django.urls import path
from .views import ResetPasswordView, ResetPasswordConfirmView, RegisterUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('user_create/', RegisterUserView.as_view(), name='user_create'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    path('reset_password_confirm/', ResetPasswordConfirmView.as_view(), name='reset_password_confirm'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]