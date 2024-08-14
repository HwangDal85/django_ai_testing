from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('chat/', views.ChatView.as_view(), name='chat'),
]