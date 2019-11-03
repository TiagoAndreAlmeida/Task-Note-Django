from rest_framework import viewsets, serializers, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from api_v1.serializers import UserProfileSerializer
from task_app.models import UserProfile

class UserProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer