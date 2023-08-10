from django.db import models
from posts.models.models import PostBase


class Report(PostBase):
    class ReportTypeChoice(models.IntegerChoices):
        ABUSE = 1, "Abuse"
        SEXUAL = 2, "Sexual content"
        MISINFO = 3, "Misinformation"
        ETC = 4, "Etc"

    target_post = models.OneToOneField(
        'posts.TargetPost', null=False, blank=False, on_delete=models.CASCADE)
    report_type = models.PositiveSmallIntegerField(
        choices=ReportTypeChoice.choices,
        default=ReportTypeChoice.ETC)
    content = models.TextField(default="", blank=True)
