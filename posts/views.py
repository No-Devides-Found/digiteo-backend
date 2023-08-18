from .serializers import *
from .models import *
from django.db.models import Q
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response


class PracticeList(APIView):
    def get(self, request, **kwargs):
        search_title = request.GET.get('search-title')
        search_nickname = request.GET.get('search-nickname')
        search_tag = request.GET.get('search-tag')

        # 검색어가 없는 경우
        if (search_title == None and search_nickname == None):
            queryset = Practice.objects.all().order_by('-created_at')
        # 제목 검색
        elif search_title:
            queryset = Practice.objects.filter(
                Q(title__icontains=search_title)).order_by('-created_at')
        # 닉네임 검색
        elif search_nickname:
            queryset = Practice.objects.filter(
                Q(user__profile__nickname__icontains=search_nickname)).order_by('-created_at')
        # 태그 검색
        elif search_tag:
            queryset = Practice.objects.filter(
                Q(practice_tag_map__tag__name__icontains=search_tag)).order_by('-created_at')
        # 제목 + 닉네임검색
        else:
            queryset = Practice.objects.filter(
                Q(title__icontains=search_title) |
                Q(title__icontains=search_nickname) |
                Q(user__profile__nickname__icontains=search_title) |
                Q(user__profile__nickname__icontains=search_nickname)
                ).order_by('-created_at')
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


class LikedViewSet(viewsets.ModelViewSet):
    queryset = Liked.objects.all()
    serializer_class = LikedSerializer