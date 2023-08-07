from django.db import models

class Program(models.Model):
    title = models.CharField(max_length=50, unique=True)
    introduce = models.TextField()
    review = models.TextField(default="")
    assignment_id = models.ForeignKey("Assignment", on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="programs/thumbnail/%Y%m%d")
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)
    tag = models.ManyToManyField("Tags", related_name="Program_Tags_Map")


class Category(models.Model):
    # 카테고리 명
    category = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.category


class Contents(models.Model):
    program_id = models.ForeignKey("Program", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    order = models.IntegerField()


class Quiz(models.Model):
    program_id = models.ForeignKey("Program", on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.BooleanField()


class Assignment(models.Model):
    submit = models.FileField(upload_to="programs/assignment/submit/%Y%m%d", blank=True, null=True)
    guide_text = models.TextField(default="")
    guide_ref = models. FileField(upload_to="programs/assignment/guide_ref/%Y%m%d")
    title = models.CharField(max_length=50)


class Tags(models.Model):
    tag = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.tag