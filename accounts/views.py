from django.shortcuts import render
from .serializers import UserSerializer, ProfileSerializer
from .models import User, Profile
from rest_framework import generics, viewsets


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(request):
        pass
