from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription_list, name='subscription_list'),
    path('buy/', views.buy_subscription, name='buy_subscription'),
    path('extend/<int:pk>/', views.extend_subscription, name='extend_subscription'),
    path('delete/<int:pk>/', views.delete_subscription, name='delete_subscription'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
]