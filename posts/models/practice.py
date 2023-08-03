from django.db import models
from posts.models.models import PostBase


# 창작물
class Creation(models.Model):
    practice = models.ForeignKey(
        "posts.Practice", on_delete=models.CASCADE)
    order = models.IntegerField(null=False)
    filename = models.CharField(max_length=30)
    file = models.FileField(
        upload_to="practice/creation/%Y%m%d", max_length=100)  # FIXME: 추후 base64로 변경 가능
    file_type = models.CharField(max_length=10)


# 실습(창작마루)
class Practice(PostBase):
    title = models.CharField(max_length=30)
    thumbnail = models.ImageField(
        upload_to="practice/thumbnail/%Y%m%d", blank=True, max_length=None)
    create_story = models.TextField()
    review = models.TextField()
