from django.urls import path

from rest_framework import routers

from .views import *


urlpatterns = [
    path('tasklist', TaskListApiView.as_view(), name='apitasklist')


]