from .serializers import *
from .models import *
from rest_framework import viewsets, permissions

class ProgramViewSet(viewsets.ModelViewSet):
	queryset = Program.objects.all()
	serializer_class = ProgramSerializer


class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class ContentsViewSet(viewsets.ModelViewSet):
	queryset = Contents.objects.all()
	serializer_class = ContentsSerializer


class QuizViewSet(viewsets.ModelViewSet):
	queryset = Quiz.objects.all()
	serializer_class = QuizSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
	queryset = Assignment.objects.all()
	serializer_class = AssignmentSerializer


class TagsViewSet(viewsets.ModelViewSet):
	queryset = Tags.objects.all()
	serializer_class = TagsSerializer

