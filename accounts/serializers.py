from rest_framework import serializers
from .models import User, Profile
from dj_rest_auth.registration.serializers import RegisterSerializer


class ProfileSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        profile = Profile.objects.create(**validated_data)
        return profile

    class Meta:
        model = Profile
        fields = ['nickname', 'birth', 'job', 'grade', 'department']


class UserSerializer(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     user = User.objects.create_user(
    #         email=validated_data['email'],
    #         username=validated_data['username'],
    #         password=validated_data['password']
    #     )
    #     return user

    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class CustomRegisterSerializer(RegisterSerializer):
    profile = ProfileSerializer(many=False)

    def custom_signup(self, request, user):
        profile_data = self.validated_data.get('profile', '')
        new_profile = Profile.objects.create(user=user, **profile_data)
