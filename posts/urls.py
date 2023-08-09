from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('practice', views.PracticeViewSet)
router.register('QnA', views.QnAViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
