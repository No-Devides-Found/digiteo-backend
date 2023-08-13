from .serializers import *
from .models import *
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

class ProgramViewSet(viewsets.ModelViewSet):
	queryset = Program.objects.all()
	serializer_class = ProgramSerializer
	


# class CategoryViewSet(viewsets.ModelViewSet):
# 	queryset = Category.objects.all()
# 	serializer_class = CategorySerializer


class ContentsViewSet(viewsets.ModelViewSet):
	queryset = Contents.objects.all()
	serializer_class = ContentsSerializer


class QuizViewSet(viewsets.ModelViewSet):
	queryset = Quiz.objects.all()
	serializer_class = QuizSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
	queryset = Assignment.objects.all()
	serializer_class = AssignmentSerializer


# class TagViewSet(viewsets.ModelViewSet):
# 	queryset = Tag.objects.all()
# 	serializer_class = TagSerializer


# class Program_Tag_MapViewSet(viewsets.ModelViewSet):
# 	queryset = Program_Tag_Map.objects.all()
# 	serializer_class = Program_Tag_MapSerializer


# class AttendRankViewSet(viewsets.ViewSet):
# 	queryset = Program.objects.all()
# 	serializer_class = AttendRankSerializer
# 	permission_classes = [permissions.AllowAny]


class AttendRankViewSet(viewsets.ViewSet):
    queryset = Program.objects.all()
    serializer_class = AttendRankSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        programs = Program.objects.all()
        serializer = ProgramSerializer(programs, many=True)

        sorted_programs = sorted(serializer.data, key=lambda x: x['participants_cnt'], reverse=True)
        top_5_programs = sorted_programs[:5]

        return Response(top_5_programs)