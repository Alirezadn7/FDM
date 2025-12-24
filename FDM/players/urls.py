# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 21:02:55 2025

@author: Asus
"""

from django.urls import path
from . import views  

urlpatterns = [
   
    path('', views.showView, name='show_url'),

    
    path('add-player/', views.PlayerFormView, name='player_form_url'),
    path('update-player/<int:f_pid>/', views.PlayersUpdateView, name='player_update_url'),
    path('delete-player/<int:f_pid>/', views.PlayerDeleteView, name='player_delete_url'),

   
    path('add-stats/', views.StatsFormView, name='stats_form_url'),
    path('update-stats/<int:stat_id>/', views.StatsUpdateView, name='stats_update_url'),
    path('delete-stats/<int:stat_id>/', views.StatsDeleteView, name='stats_delete_url'),
]
