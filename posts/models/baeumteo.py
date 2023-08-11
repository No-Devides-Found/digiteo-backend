from django.db import models
from .models import PostBase


# 배움터
class QnA(PostBase):
    title = models.CharField(max_length=50)
    content = models.TextField()


class QnA_Image(models.Model):
    qna = models.ForeignKey(QnA, on_delete=models.CASCADE)
    file = models.ImageField(
        upload_to="posts/qna/%Y%m%d", blank=True, null=True)


class Agora(PostBase):
    class AgoraTypeChoice(models.IntegerChoices):
        # 자유토론
        DISCUSSION = 1, "Discussion"
        # 찬반논쟁
        DEBATE = 2, "Debate"

    title = models.CharField(max_length=50)
    thumbnail = models.ImageField(
        upload_to="posts/agora/%Y%m%d", blank=True, null=True)
    agora_type = models.PositiveSmallIntegerField(
        choices=AgoraTypeChoice.choices)
    summary = models.TextField(default="")
    my_opinion = models.TextField(default="")