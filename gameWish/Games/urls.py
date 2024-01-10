from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.fetch_games_data, name='getData'),
    path('search/<int:id>', views.game_details, name='game_detail'),
    path('add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
]
