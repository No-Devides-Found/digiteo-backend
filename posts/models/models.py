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


class TargetPost(models.Model):
    # ['qna', 'practice', ...]
    target_post_type = models.CharField(max_length=10, null=False, default="")

    qna = models.ForeignKey(
        "posts.QnA", null=True, blank=True, on_delete=models.CASCADE)
    practice = models.ForeignKey(
        "posts.Practice", null=True, blank=True, on_delete=models.CASCADE)
    # 모델 개발되는대로 여기 추가하기

    @property
    def target(self):
        if self.qna_id is not None:
            return self.qna
        if self.practice_id is not None:
            return self.practice

        raise AssertionError("Target is not set")




# # 댓글
# class Comment(PostBase):
#     pass


# # 강의평
# class Evaluation(PostBase):
#     pass
