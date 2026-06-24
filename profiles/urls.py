from django.urls import path
from . import views
from .views import register, profile

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]