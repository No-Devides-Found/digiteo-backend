from .serializers import *
from .models.practice import *
from rest_framework import viewsets, permissions


class PracticeViewSet(viewsets.ModelViewSet):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer
