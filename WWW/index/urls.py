from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('team/', views.team_list, name='team_list'),
]