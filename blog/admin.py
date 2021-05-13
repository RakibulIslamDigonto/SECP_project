from django.contrib import admin
from .models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):

    list_display = [
        'thumbnail',
        'title',
        'short_discription',
        'discription',
        'creation'
    ]

admin.site.register(Blog, BlogAdmin)