from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('program', views.ProgramViewSet)
router.register('category', views.CategoryViewSet)
router.register('contents', views.ContentsViewSet)
router.register('quiz', views.QuizViewSet)
router.register('assignment', views.AssignmentViewSet)
router.register('tags', views.TagsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]