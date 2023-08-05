from django.db import models

class Program(models.Model):
    title = models.CharField(max_length=50, unique=True)
    introduce = models.TextField(max_length=500)
    review = models.TextField(max_length=500, default="")
    assignment_id = models.ForeignKey("Assignment", on_delete=models.CASCADE)
    thumbnail = models.ImageField
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)


class Category(models.Model):
    # 카테고리 명
    category = models.CharField(max_length=10, unique=True)


#  논의 필요
# class Quiz(models.Model):
#     program_id = models.ForeignKey("Program", on_delete=models.CASCADE)
#     question = models.TextField(max_length=500)
#     passage = models.TextField(max_length=500, default="")
#     answer = 

class Contents(models.Model):
    program_id = models.ForeignKey("Program", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    order = models.IntegerField


# 논의 필요
# class Assignment(models.Model):
#     pass