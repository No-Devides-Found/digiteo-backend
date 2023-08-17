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
    agora = models.ForeignKey(
        "posts.Agora", null=True, blank=True, on_delete=models.CASCADE)
    tip = models.ForeignKey(
        "posts.Tip", null=True, blank=True, on_delete=models.CASCADE)

    @property
    def target(self):
        if self.qna_id is not None:
            return self.qna
        if self.practice_id is not None:
            return self.practice
        if self.agora_id is not None:
            return self.agora
        if self.tip_id is not None:
            return self.tip

        raise AssertionError("Target is not set")


# 댓글
class Comment(PostBase):
    content = models.TextField(null=False, default="")
    target_post = models.OneToOneField(
        "posts.TargetPost", on_delete=models.CASCADE, null=False)