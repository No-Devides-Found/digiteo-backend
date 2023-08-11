from django.contrib import admin
from .models.practice import Practice, Creation
from .models.models import TargetPost
from .models.baeumteo import QnA, QnA_Image, Agora
from .models.nanumteo import Tip, Tip_Image, Tip_Tag_Map

admin.site.register(Practice)
admin.site.register(Creation)
admin.site.register(QnA)
admin.site.register(QnA_Image)
admin.site.register(TargetPost)
admin.site.register(Agora)
admin.site.register(Tip)
admin.site.register(Tip_Image)
admin.site.register(Tip_Tag_Map)