from rest_framework import views, serializers, status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api_v1.serializers import UserProfileSerializer
from task_app.models import UserProfile

class UserProfileView(views.APIView):

    def post(self, request, *args, **kwargs):
        try:
            _username = request.data["email"] or None
            user = User.objects.get(username=_username)
            return Response({"message": "Já existe um usuário com esse E-mail"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        except User.DoesNotExist:
            user = User.objects.create_user(username=request.data["email"], password=request.data["password"])
            data = {
                "user": user.id,
                "name": request.data["name"],
                "photo": request.data["photo"]
            }
            serializer = UserProfileSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    
    def patch(self, request):
        try:
            user_profile = UserProfile.objects.get(pk=request.data["id"])
            name = request.data["name"]
            serializer = UserProfileSerializer(user_profile, data={"name": name}, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"message": "user does not exist"}, status=status.HTTP_404_NOT_FOUND)

    @api_view(['POST'])
    def auth_login(request):
        user = authenticate(username=request.data["username"], password=request.data["password"])
        if user is None:
            raise serializers.ValidationError({"message":"Invalido Username/Password"})
        
        profile = UserProfile.objects.get(user__pk=user.pk)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)