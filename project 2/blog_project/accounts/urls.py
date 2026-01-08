"""Defines URL patterns for registration"""
from django.urls import include, path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', views.registration, name='registration'),
]