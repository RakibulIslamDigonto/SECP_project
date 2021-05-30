from django.contrib import admin
from .models import Blog, Comment,Category
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name','slug']
    prepopulated_fields ={'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class BlogAdmin(SummernoteModelAdmin):

    list_display = [
        'thumbnail',
        'title',
        'short_discription',
        'discription',
        'creation'
    ]

    summernote_fields = ('discription',)

admin.site.register(Blog, BlogAdmin)

class CommentAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'body'
    ]

admin.site.register(Comment, CommentAdmin)