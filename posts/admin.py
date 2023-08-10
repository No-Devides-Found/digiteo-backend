from django.contrib import admin
from .models.practice import Practice, Creation
from .models.models import TargetPost
from .models.baeumteo import QnA, QnA_Image


admin.site.register(Practice)
admin.site.register(Creation)
admin.site.register(QnA)
admin.site.register(TargetPost)
