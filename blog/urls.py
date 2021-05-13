from functools import partial
from django.urls import path, include
from .import views

app_name = 'my_album'

urlpatterns = [
     path('', views.blog_list, name = 'blog_list'),

]
