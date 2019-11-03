from rest_framework import serializers
from django.contrib.auth.models import User

from task_app.models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="username")
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ("id", "email", "password")

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = UserProfile
        fields = ("name", "user")

    def create(self, validated_data):
        #first get user field from json request
        user_data = validated_data.pop('user')
        #create a user django after atatch in profile model
        user = User.objects.create_user(username=user_data['username'], password=user_data['password'])
        #create profile instance using user.
        profile = UserProfile.objects.create(user=user, **validated_data)
        return profile