from django.core import paginator
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from django.http import HttpResponseRedirect
from .models import Blog, Category
from django.db.models import Q, query
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

def blog_list(request, category_slug= None):
    category = None
    categories = Category.objects.all()
    blog = Blog.objects.all()
    
    paginator = Paginator(blog, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        blog = blog.filter(category=category)

        paginator = Paginator(blog, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    context = {
        'blogs':blog,
        'category':category,
        'categories':categories,
        'page_obj':page_obj
    }
    return render(request, 'blog/blog.html', context)


def blog_details(request, slug):

    blog = Blog.objects.get(slug=slug)
           #gattit
    similar_blogs = blog.tags.similar_objects()[:2]
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
        #gattit
        'similar_blogs':similar_blogs,
        'comments':comments

    }
    return render(request, 'blog/details.html', context)


def search_blog(request):

    queryset = Blog.objects.all()
    query = request.GET.get('q')

    paginator = Paginator(queryset, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if query:
        queryset=queryset.filter(
            Q(title__icontains = query) | Q(short_discription__icontains = query) | Q(discription__icontains = query)
        ).distinct()
    
    context = {
        'queryset': queryset,
        'query': query
    }

    return render(request, 'blog/search.html', context)


