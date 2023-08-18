from .serializers import *
from .models import *
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ContentsViewSet(viewsets.ModelViewSet):
    queryset = Contents.objects.all()
    serializer_class = ContentsSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class AttendRankViewSet(viewsets.ViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        programs = Program.objects.all()
        serializer = ProgramSerializer(programs, many=True) # context={'request':request}

        sorted_programs = sorted(
            serializer.data, key=lambda x: x['participants_cnt'], reverse=True)
        top_5_programs = sorted_programs[:5]

        return Response(top_5_programs)


class MyProgramListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id, format=None):
        program_user_maps = Program_User_Map.objects.filter(
            user=user_id)
        program_ids = program_user_maps.values_list('program_id', flat=True)
        programs = Program.objects.filter(id__in=program_ids)
        serializer = ProgramSerializer(programs, many=True)
        return Response({"program_user_maps": list(program_user_maps.values()), "programs": serializer.data}, status=status.HTTP_200_OK)


# class ProgramContentViewSet(viewsets.ViewSet):
#     queryset = Program.objects.all()
#     serializer_class = ProgramContentSerializer

#     def list(self, request, pk=None):
#         program = self.get_object()
#         contents = program.contents.all()

#         serializer = self.serializer_class(program)
#         content_serializer = ContentsSerializer(contents, many=True)

#         return Response({
#             'program_info': serializer.data,
#             'contents': content_serializer.data
#         })

class ProgramContentViewSet(viewsets.ViewSet):
    serializer_class = ProgramContentSerializer

    def list(self, request, pk=None):
        program = Program.objects.get(pk=pk)  # 해당 프로그램 가져오기
        contents = Contents.objects.filter(program=program)  # 해당 프로그램에 속하는 컨텐츠들

        serializer = self.serializer_class(program)
        content_serializer = ContentsSerializer(contents, many=True)

        return Response({
            'program_info': serializer.data,
            'contents': content_serializer.data
        })