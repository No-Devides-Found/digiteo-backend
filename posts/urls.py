from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('QnA', views.QnAViewSet)
router.register('Agora', views.AgoraViewSet)
router.register('Tip', views.TipViewSet)
router.register('Evaluation', views.EvaluationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('practice-list/', views.PracticeList.as_view()),
]
