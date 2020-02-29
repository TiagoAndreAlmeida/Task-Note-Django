from rest_framework import serializers
from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64ImageField

from task_app.models import UserProfile, Task
from task_app.utils import EmailUnavailable

class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="username")
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ("id", "email", "password")

class UserProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer(required=True)
    #using extra drf field to save base64 images
    photo = Base64ImageField(required=True)
    class Meta:
        model = UserProfile
        fields = ("id", "name", "user", "photo")
        # depth = 1

    # def create(self, validated_data):
    #     #first get user field from json request
    #     user_data = validated_data.pop('user')

    #     #create a user django after atatch in profile model
    #     user = User(username=user_data['username'])
    #     user.set_password(user_data['password'])
    #     user.save()
             
    #     #create profile instance using user.
    #     profile = UserProfile.objects.create(user=user, **validated_data)
    #     return profile

    # def validate_user(self, value):
    #     if(User.objects.filter(username=value['username']).exists()):
    #         raise EmailUnavailable()
    #     return value

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "owner", "description", "title", "dead_line", "done")
    