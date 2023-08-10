from .serializers import *
from .models import *
from rest_framework import viewsets, permissions


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
