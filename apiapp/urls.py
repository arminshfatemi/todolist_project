from django.urls import path

from rest_framework import routers

from .views import *


urlpatterns = [
    path('task-list/', TaskListApiView.as_view(), name='api-task-list'),
    path('task-list/<int:pk>/', TaskRUDApiView.as_view(), name='api-task-list-RUD'),


]