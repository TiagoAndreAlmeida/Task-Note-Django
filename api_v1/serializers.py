from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import status
from drf_extra_fields.fields import Base64ImageField
from rest_framework.exceptions import APIException

from task_app.models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="username")
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ("id", "email", "password")

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    #using extra drf field to save base64 images
    photo = Base64ImageField(required=True)
    class Meta:
        model = UserProfile
        fields = ("name", "user", "photo")

    def create(self, validated_data):
        #first get user field from json request
        user_data = validated_data.pop('user')

        #create a user django after atatch in profile model
        user = User(username=user_data['username'])
        user.set_password(user_data['password'])
        user.save()
             
        #create profile instance using user.
        profile = UserProfile.objects.create(user=user, **validated_data)
        return profile

    def validate_user(self, value):
        if(User.objects.filter(username=value['username']).exists()):
            print("REPETIDO")
            raise APIException(detail="Usuário já exe", code=status.HTTP_406_NOT_ACCEPTABLE)
        print("PASSOU!")
        return value