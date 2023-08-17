from .serializers import *
from .models import *
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response


class PracticeViewSet(viewsets.ModelViewSet):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer


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
