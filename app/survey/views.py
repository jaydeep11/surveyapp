# from user import models

# from common.decorators import meta_data_response, session_authorize,\
#     catch_exception
# from common.exceptions import InvalidSerializerInputException ,NotAcceptableError

from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models

# from .services import document_upload_service
# from .services.social_login_service import GoogleLoginService,LinkedInLoginService
from django.conf import settings
# from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db import transaction
from django.shortcuts import redirect
from django.views.generic.base import RedirectView
from . import serializers
import jwt

#User APIs
class UserWelcome(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {
                "message": "Welcome to the Survey API Server, deployed via heroku --V.1.0"
            },
            status=status.HTTP_200_OK)

class UserLoginView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            session_data = serializer.save()
            return Response(session_data, status=status.HTTP_200_OK)
        return Response({},status=status.HTTP_400_BAD_REQUEST)