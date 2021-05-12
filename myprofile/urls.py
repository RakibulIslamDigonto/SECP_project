from functools import partial
from django.urls import path, include
from .import views

app_name = 'myprofile'

urlpatterns = [
     path('', views.homepage, name = 'homepage'),
]