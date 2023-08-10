from .serializers import *
from .models import *
from rest_framework import viewsets, permissions


class PracticeViewSet(viewsets.ModelViewSet):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer


class QnAViewSet(viewsets.ModelViewSet):
    queryset = QnA.objects.all()
    serializer_class = QnASerializer
