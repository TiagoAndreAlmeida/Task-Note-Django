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
    user = UserSerializer()
    photo = Base64ImageField()
    
    class Meta:
        model = UserProfile
        fields = ("id", "name", "photo", "email", 'user')
        extra_kwargs = {'user': {'write_only': True}}

    def create(self, validated_data):
        #first get user field from json request
        user_data = validated_data.pop('user')
        print(user_data)
        user = User.objects.create_user(**user_data)
        user.save()
             
        #create profile instance using user.
        profile = UserProfile.objects.create(user=user, **validated_data)
        return profile

    # def validate_user(self, value):
    #     if(User.objects.filter(username=value['username']).exists()):
    #         raise EmailUnavailable()
    #     return value

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "owner", "description", "title", "dead_line", "done")
    