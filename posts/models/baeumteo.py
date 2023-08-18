from django.db import models
from posts.models.models import PostBase


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
    class MyOpinionTypeChoice(models.IntegerChoices):
        # 찬성
        PROS = 1, "Pros"
        # 반대
        CONS = 2, "Cons"

    title = models.CharField(max_length=50)
    thumbnail = models.ImageField(
        upload_to="posts/agora/%Y%m%d", blank=True, null=True)
    agora_type = models.PositiveSmallIntegerField(
        choices=AgoraTypeChoice.choices)
    summary = models.TextField(default="")
    my_opinion = models.TextField(default="")
    my_opinion_type = models.PositiveSmallIntegerField(
        choices=MyOpinionTypeChoice.choices, blank=True, null=True)
    pros = models.TextField(default="", blank=True, null=True)
    cons = models.TextField(default="", blank=True, null=True)


class AgoraCommentLiked(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    agora_comment = models.OneToOneField(
        "posts.Comment", on_delete=models.CASCADE, null=False)