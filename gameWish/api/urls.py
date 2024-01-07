from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetch_game_data, name='getData'),
]
