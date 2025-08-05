from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('<int:pk>/', views.service_detail, name='service_detail'),
    path('<int:pk>/free-valuation/', views.free_valuation, name='free_valuation'),
    path('<int:pk>/schedule-meeting/', views.schedule_meeting, name='schedule_meeting'),
]