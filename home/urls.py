from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play_audio', views.play_audio, name='play_audio')
]