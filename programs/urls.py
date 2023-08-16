from django.urls import path, include
from . import views
from rest_framework import routers

# User별 program
# program_detail = views.ProgramViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
# })

# programs/program
router_program = routers.DefaultRouter()
router_program.register('program', views.ProgramViewSet)

# programs/attend_rank
router_attend_rank = routers.DefaultRouter()
router_attend_rank.register('attend_rank', views.AttendRankViewSet)

# programs/myprogram
# router_myprogram = routers.DefaultRouter()
# router_myprogram.register('myprogram', views.MyProgramViewSet, basename='myprogram')

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
    # path('', include(router_myprogram.urls)),
    # path('myprogram/<int:pk>/', program_detail),
    path('myprogram/<int:user_id>/', views.UserProgramListView.as_view(), name='user-program-list'),
]