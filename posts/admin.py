from django.contrib import admin
from .models.practice import Practice, Creation, Practice_Tag_Map
from .models.models import TargetPost, Comment, PostLiked
from .models.baeumteo import QnA, QnA_Image, Agora, AgoraCommentLiked
from .models.nanumteo import Tip, Tip_Image, Tip_Tag_Map, TipCommentLiked
from .models.evaluation import Evaluation

admin.site.register(Practice)
admin.site.register(Creation)
admin.site.register(QnA)
admin.site.register(QnA_Image)
admin.site.register(TargetPost)
admin.site.register(Agora)
admin.site.register(Tip)
admin.site.register(Tip_Image)
admin.site.register(Tip_Tag_Map)
admin.site.register(Evaluation)
admin.site.register(Practice_Tag_Map)
admin.site.register(Comment)
admin.site.register(PostLiked)
admin.site.register(AgoraCommentLiked)
admin.site.register(TipCommentLiked)