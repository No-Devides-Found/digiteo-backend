from django.urls import path, include
from . import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('signup/', views.UserCreate.as_view()),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration', include('dj_rest_auth.registration.urls')),
    path('', include('allauth.urls')),
]
