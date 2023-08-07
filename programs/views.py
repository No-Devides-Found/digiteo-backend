from .serializers import *
from .models import *
from rest_framework import viewsets, permissions

class ProgramViewSet(viewsets.ModelViewSet):
	queryset = Program.objects.all()
	serializer_class = ProgramSerializer

