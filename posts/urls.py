from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('practice', views.PracticeViewSet)
router.register('QnA', views.QnAViewSet)
router.register('Agora', views.AgoraViewSet)
router.register('Tip', views.TipViewSet)
router.register('Evaluation', views.EvaluationViewSet)

urlpatterns = [
    path('mypost/<int:user_id>/',
         views.MyPostsListView.as_view(), name='user-post-list'),
]
