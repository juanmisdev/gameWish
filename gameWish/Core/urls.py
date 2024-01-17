from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('profile/<int:pk>', views.profile, name = 'profile'),
    path('profile/edit', views.edit_profile, name = 'edit_profile'),
    path('remove_from_wishlist/<int:game_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]