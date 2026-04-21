from django.urls import path
from .views import RegisterView, TestView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns=[
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('test/', TestView.as_view()),
]