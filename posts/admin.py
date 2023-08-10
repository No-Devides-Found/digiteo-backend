from django.contrib import admin
from .models import Practice, Creation, QnA
from .models.models import TargetPost


admin.site.register(Practice)
admin.site.register(Creation)
admin.site.register(QnA)
admin.site.register(TargetPost)
