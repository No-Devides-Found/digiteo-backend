from django.db import models


class PostBase(models.Model):
    class Meta:
        abstract = True
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FileTypeChoice(models.IntegerChoices):
    VIDEO = 1, "Video"
    IMAGE = 2, "Image"
    VOICE = 3, "Voice"
    DOCUMENT = 4, "Document"

# # 배움터
# class QnA(PostBase):
#     pass


# # 나눔터
# class Tip(PostBase):
#     pass


# # 댓글
# class Comment(PostBase):
#     pass


# # 강의평
# class Evaluation(PostBase):
#     pass
