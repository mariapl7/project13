from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import User


class ResetPasswordView(generics.GenericAPIView):
    """Представление для запроса сброса пароля.
    Пользователь отправляет свой email и получает ссылку для сброса пароля.
    Пример запроса:
      POST /users/reset_password/
      {
          "email": "example@mail.com"
      }
    Ответ:
      {
          "message": "Password reset link sent."
      }
      или
      {
          "error": "User with this email does not exist."
      }"""

    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")

        try:
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = f"http://yourfrontend.com/reset_password/{uidb64}/{token}/"

            send_mail(
                subject="Password Reset Request",
                message=f"Click the link to reset your password: {reset_link}",
                from_email="your_email@gmail.com",
                recipient_list=[email],
            )
            return Response({"message": "Password reset link sent."}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist."}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordConfirmView(generics.GenericAPIView):
    """Представление для подтверждения сброса пароля.
    Пользователь отправляет uid и токен вместе с новым паролем для его установки.
    Пример запроса:
      POST /users/reset_password_confirm/
      {
          "uid": "uid",
          "token": "token",
          "new_password": "P4$$W0RD"
      }
    Ответ:
      {
          "message": "Password has been reset successfully."
      }
      или
      {
          "error": "Invalid token or uid."
      }"""


permission_classes = [AllowAny]


def force_text(param):
    pass


def post(self, request):
    uidb64 = request.data.get("uid")
    token = request.data.get("token")
    new_password = request.data.get("new_password")

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        if default_token_generator.check_token(user, token):
            user.set_password(new_password)
            user.save()
            return Response({"message": "Password has been reset successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid token or uid."}, status=status.HTTP_400_BAD_REQUEST)

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return Response({"error": "Invalid token or uid."}, status=status.HTTP_400_BAD_REQUEST)
