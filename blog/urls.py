from functools import partial
from django.urls import path, include
from .import views

app_name = 'my_album'

urlpatterns = [
     path('', views.blog_list, name = 'blog_list'),
     path('blog/<slug>/', views.blog_details, name = 'blog_details'),
     path('search/', views.search_blog, name = 'search_blog'),


]
