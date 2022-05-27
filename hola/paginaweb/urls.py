from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('docker/',docker.as_view(), name = 'docker'),
    path('ubuntu/',ubuntu.as_view(), name = 'ubuntu'),
]
