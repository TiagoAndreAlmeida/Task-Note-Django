from rest_framework import serializers
from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64ImageField

from task_app.models import UserProfile, Task
from task_app.utils import EmailUnavailable

class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="username")
    class Meta:
        model = User
        fields = ("id", "email", "password")
        extra_kwargs = {'password': {'write_only': True}}

class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    photo = Base64ImageField()
    
    class Meta:
        model = UserProfile
        fields = ("id", "name", "photo", "email", 'password')

    def create(self, validated_data):
        """first get remove password param with pop operator 
        from json request because it dont exist on Profile model 
        and is used only for write"""
        password = validated_data.pop('password', None)
        user = User.objects.create_user(username=validated_data.get("email", None), password=password)
        user.save()
             
        #create profile instance using user.
        profile = UserProfile.objects.create(user=user, **validated_data)
        return profile

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "owner", "description", "title", "dead_line", "done")
    