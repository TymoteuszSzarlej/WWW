from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('start/', views.start_conversation, name='start_conversation'),
    path('conversation/<int:pk>/', views.conversation_detail, name='conversation_detail'),
    path('conversation/<int:pk>/send-message/', views.send_message, name='send_message'),
]