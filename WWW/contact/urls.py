from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('start/', views.contact, name='start_conversation'),
    path('conversation/<int:pk>/', views.contact, name='conversation_detail'),
    path('conversation/<int:pk>/send-message/', views.contact, name='send_message'),
]