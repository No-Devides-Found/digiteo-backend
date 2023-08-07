from django.db import models
from posts.models.models import PostBase, FileTypeChoice


# 창작물
class Creation(models.Model):
    practice = models.ForeignKey(
        "posts.Practice", on_delete=models.CASCADE, related_name="creations")
    order = models.IntegerField(null=False, default=0)
    filename = models.CharField(max_length=30)
    file = models.TextField()  # base64
    file_type = models.PositiveSmallIntegerField(
        choices=FileTypeChoice.choices,
        default=FileTypeChoice.VIDEO)


# 실습(창작마루)
class Practice(PostBase):
    title = models.CharField(max_length=30)
    thumbnail = models.ImageField(
        upload_to="practice/thumbnail/%Y%m%d", blank=True, max_length=None)
    create_story = models.TextField()
    review = models.TextField()
