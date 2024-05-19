# posts/urls.py

from django.urls import path
from .views import post_list, post_create, post_delete

urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', post_create, name='post_create'),
    path('delete/<int:pk>/', post_delete, name='post_delete'),
]
