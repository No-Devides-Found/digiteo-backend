from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import PostBase


# 강의평
class Evaluation(PostBase):
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    content = models.TextField()
    # program_user_map = models.OneToOneField('programs.Program_User_Map', on_delete=models.PROTECT)
