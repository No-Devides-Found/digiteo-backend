from django.urls import path, include
from . import views
from rest_framework import routers

# programs/program
router_program = routers.DefaultRouter()
router_program.register('program', views.ProgramViewSet)

# programs/attend_rank
router_attend_rank = routers.DefaultRouter()
router_attend_rank.register('attend_rank', views.AttendRankViewSet)


router = routers.DefaultRouter()
router.register('contents', views.ContentsViewSet)
router.register('quiz', views.QuizViewSet)
router.register('assignment', views.AssignmentViewSet)
# router.register('tag', views.TagViewSet)
# router.register('category', views.CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(router_program.urls)),
    path('', include(router_attend_rank.urls)),
]