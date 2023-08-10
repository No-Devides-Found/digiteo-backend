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
