from rest_framework import views, serializers, status, viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api_v1.serializers import UserProfileSerializer
from task_app.models import UserProfile

class UserProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @api_view(['POST'])
    def auth_login(request):
        user = authenticate(username=request.data["username"], password=request.data["password"])
        if user is None:
            raise serializers.ValidationError({"message":"Invalido Username/Password"})
        
        profile = UserProfile.objects.get(user__pk=user.pk)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
