from django.contrib import admin
from .models import Practice, Creation
from .models.models import QnA
# Register your models here.

admin.site.register(Practice)
admin.site.register(Creation)
admin.site.register(QnA)