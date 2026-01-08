"""Defines URL patterns for blog_site"""
from django.urls import path

from . import views

app_name = 'blog_site'
urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<int:blog_id>', views.blog, name='blog'),
    path('blogs/create_blog/', views.create_blog, name='create_blog'),
    path('blogs/create_entry/<int:blog_id>', views.create_entry, name='create_entry'),
    path('blogs/edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]
