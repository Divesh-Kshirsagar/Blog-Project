from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'Blogs'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.blog_create_view, name='create'),
    path('myblogs/', views.user_blog_view, name='myblogs'),
    path('blogs/', views.blogs_view, name='blogs'),
    path('blog_post/<int:id>/', views.blog_post, name='blog_post'),
    path('myblog/<int:id>/', views.user_blog_post, name='myblog'),
    path('delete_blog_post/<int:id>/', views.delete_blog_post, name='delete_blog_post'),
    path('update_blog_post/<int:id>/', views.update_blog_post, name='update_blog_post'),
]