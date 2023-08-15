from django.urls import path, include
from . import views

# Profile detail 보여주기 + 수정
profile_detail = views.ProfileViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
})


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('signup/', views.UserCreate.as_view()),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration', include('dj_rest_auth.registration.urls')),
    path('', include('allauth.urls')),
    path('profile/<int:pk>/', profile_detail),

]
