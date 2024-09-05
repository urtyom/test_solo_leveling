from django.urls import path
from . import views

urlpatterns = [
    path('export/', views.export_player_levels_to_csv, name='export_player_levels'),
]
