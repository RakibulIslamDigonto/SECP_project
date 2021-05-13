from django.shortcuts import render
from .models import Blog

# Create your views here.

def blog_list(request):
    blog = Blog.objects.all()
    context = {
        'blogs':blog

    }
    return render(request, 'blog/blog.html', context)