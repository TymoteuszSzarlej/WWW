from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/add-comment/', views.add_comment, name='add_comment'),
    path('post/<int:post_id>/add-review/', views.add_review, name='add_review'),
]