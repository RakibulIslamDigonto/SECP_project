


from django.shortcuts import render
from .forms import CommentForm
from django.http import HttpResponseRedirect
from .models import Blog
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

def blog_list(request):
    blog = Blog.objects.all()
    context = {
        'blogs':blog

    }
    return render(request, 'blog/blog.html', context)


def blog_details(request, slug):

    blog = Blog.objects.get(slug=slug)
    comments = blog.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.blog=blog
            new_comment.save()

            messages.success(request, 'comment submitted')
            return HttpResponseRedirect(request.path_info)

            
    else:
        comment_form = CommentForm()


    context = {
        'blog':blog,
        'comments':comments

    }
    return render(request, 'blog/details.html', context)

