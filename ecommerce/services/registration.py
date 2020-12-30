from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class RegistrationService:
    def __init__(self, payload):
        self.request_payload = payload

    def register_user(self):
        user = User(username=self.request_payload.get("username"), email=self.request_payload.get("email"))
        user.set_password(self.request_payload.get("password"))
        user.save()
        token = Token.objects.create(user=user)
        return {
            "token": token.key
        }
