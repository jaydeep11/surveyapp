from . import models
from rest_framework import serializers
from django.conf import settings
from .services.login_service import UserSessionService

class UserLoginSerializer(serializers.Serializer):
    """Custom Serializer to validate and create a Login Session."""
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        min_length=6, max_length=60, required=True)

    def save(self, **kwargs):
        """Create a new login session object or return an old one."""
        session_input = {
            'email': self.validated_data['email'],
            'password' : self.validated_data['password']
        }
        return UserSessionService(session_input).session_success_data()