from .serializers import *
from .models import *
from programs.models import *
from programs.serializers import *
from django.db.models import Q
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response


class PracticeList(APIView):
    def get(self, request, **kwargs):
        search_title = request.GET.get('search-title')
        search_nickname = request.GET.get('search-nickname')
        search_type = request.GET.get('search-type')
        queryset = Practice.objects.all().order_by('-created_at')
        # 검색어가 없는 경우
        if (search_title == None and search_nickname == None and search_type == None):
            creations = Creation.objects.filter(file_type=1)
            practice_ids = creations.values_list('practice_id', flat=True)
            queryset = queryset.filter(id__in=practice_ids)

        # 제목 검색
        if search_title:
            queryset = Practice.objects.filter(
                Q(title__icontains=search_title)).order_by('-created_at')
        # 닉네임 검색
        if search_nickname:
            queryset = Practice.objects.filter(
                Q(user__profile__nickname__icontains=search_nickname)).order_by('-created_at')
        # 파일 타입으로 검색
        if search_type:
            if search_type == "1": 
                creations = Creation.objects.filter(file_type=1)
            elif search_type == "2": 
                creations = Creation.objects.filter(file_type=2)
            elif search_type == "3": 
                creations = Creation.objects.filter(file_type=3)
            elif search_type == "4": 
                creations = Creation.objects.filter(file_type=4)
            elif search_type == "5": 
                creations = Creation.objects.filter(file_type=5)
            practice_ids = creations.values_list('practice_id', flat=True)
            queryset = queryset.filter(id__in=practice_ids)


        # 제목 + 닉네임검색
        # http://127.0.0.1:8000/posts/practice-list/?search-nickname=test&search-title=test
        # 이런식으로 같은 내용 넣어서 검색

        return Response(PracticeSerializer(queryset, many=True).data, status=status.HTTP_200_OK)


class QnAViewSet(viewsets.ModelViewSet):
    queryset = QnA.objects.all()
    serializer_class = QnASerializer


class AgoraViewSet(viewsets.ModelViewSet):
    queryset = Agora.objects.all()
    serializer_class = AgoraSerializer


class TipViewSet(viewsets.ModelViewSet):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer


class MyPostsListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id, format=None):
        qna_list = QnA.objects.filter(user=user_id)  # 유저가 작성한 qna 객체 쿼리셋
        qna_ids = qna_list.values_list('id', flat=True)
        qnas = QnA.objects.filter(id__in=qna_ids)  # qna_list에 있는 qna들 상세 정보
        qna_serializer = QnASerializer(qnas, many=True)

        agora_list = Agora.objects.filter(user=user_id)
        agora_ids = agora_list.values_list("id", flat=True)
        agoras = Agora.objects.filter(id__in=agora_ids)
        agora_serializer = AgoraSerializer(agoras, many=True)

        tip_list = Tip.objects.filter(user=user_id)
        tip_ids = tip_list.values_list("id", flat=True)
        tips = Tip.objects.filter(id__in=tip_ids)
        tip_serializer = TipSerializer(tips, many=True)

        return Response({"qna_list": list(qna_list.values()), "agora_list": list(agora_list.values()), "tip_list": list(tip_list.values()), "qnas": qna_serializer.data, "agoras": agora_serializer.data, "tips": tip_serializer.data}, status=status.HTTP_200_OK)


class PostLikedViewSet(viewsets.ModelViewSet):
    queryset = PostLiked.objects.all()
    serializer_class = LikedSerializer


class PracticeViewSet(viewsets.ModelViewSet):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer

class ProgramContentViewSet(viewsets.ViewSet):
    queryset = Contents.objects.all()
    serializer_class = ProgramContentSerializer