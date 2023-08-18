from django.urls import path, include
from . import views
from rest_framework import routers


# programs/program
router_program = routers.DefaultRouter()
router_program.register('program', views.ProgramViewSet)

# programs/attend_rank
router_attend_rank = routers.DefaultRouter()
router_attend_rank.register('attend_rank', views.AttendRankViewSet)

# programs/content_list
router_program_content = routers.DefaultRouter()
router_program_content.register('program-content', views.ProgramContentViewSet, basename='program-content')

router = routers.DefaultRouter()
router.register('contents', views.ContentsViewSet)
router.register('quiz', views.QuizViewSet)
router.register('assignment', views.AssignmentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(router_program.urls)),
    path('', include(router_attend_rank.urls)),
    path('', include(router_program_content.urls)),
    path('myprogram/<int:user_id>/', views.MyProgramListView.as_view()),
]