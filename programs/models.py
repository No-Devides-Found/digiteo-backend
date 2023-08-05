from django.db import models

class Program(models.Model):
    title = models.CharField(max_length=30, unique=True)
    introduce = models.TextField
    review = models.TextField(default="")
    # 추후 수정: assginment 모델 만들고나서 수정
    assignment_id = models.ForeignKey("", on_delete=models.CASCADE)
    thumbnail = models.ImageField
    

