# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('demo/', views.demo),
]