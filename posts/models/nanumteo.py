from django.db import models
from .models import PostBase

# 나눔터
class Tip(PostBase):
    title = models.CharField(max_length=50)
    content = models.TextField()


class Tip_Image(models.Model):
    tip = models.ForeignKey(
        Tip, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="posts/tip/%Y%m%d", blank=True, null=True)
    

class Tip_Tag_Map(models.Model):
    tip = models.ForeignKey("Tip", on_delete=models.CASCADE)
    tag = models.ForeignKey("programs.Tag", on_delete=models.CASCADE, null=True)