from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_AI, name='chat_AI'),
]
