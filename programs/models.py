from django.db import models

class Program(models.Model):
    title = models.CharField(max_length=50, unique=True)
    introduce = models.TextField()
    assignment_id = models.ForeignKey("Assignment", on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="programs/thumbnail/%Y%m%d")
    category = models.ForeignKey("Category", on_delete=models.CASCADE)


class Program_Tag_Map(models.Model):
    program = models.ForeignKey("Program", on_delete=models.CASCADE)
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE, null=True)

 
class Category(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name}"


class Contents(models.Model):
    program = models.ForeignKey("Program", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    order = models.IntegerField()


class Quiz(models.Model):
    class QuizAnswer(models.IntegerChoices):
        O = 1
        X = 2

    program = models.ForeignKey("Program", on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.PositiveSmallIntegerField(
        choices=QuizAnswer.choices)

class Assignment(models.Model):
    submit = models.FileField(upload_to="programs/assignment/submit/%Y%m%d", blank=True, null=True)
    guide_text = models.TextField(default="")
    guide_ref = models. FileField(upload_to="programs/assignment/guide_ref/%Y%m%d")
    title = models.CharField(max_length=50)


class Tag(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
    

class Program_User_Map(models.Model):
    program = models.ForeignKey("Program", on_delete=models.CASCADE)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    # 찜
    wish = models.BooleanField(default=False)
    participate = models.BooleanField(default=False)
    progress = models.IntegerField(default=0)

    def get_wish(self):
        return self.wish

    def get_participate(self):
        return self.participate
    
    def get_progress(self):
        return self.progress