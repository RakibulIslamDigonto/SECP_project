from django.db import models
from django.urls import reverse
from django.utils.translation import override
from taggit.managers import TaggableManager


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=170)
    slug = models.SlugField(max_length=170, unique=True)
    

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:blog_by_category', args={self.slug})


class Blog(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    thumbnail = models.ImageField(upload_to = 'blog/images/')
    short_discription = models.TextField()
    discription = models.TextField()
    tags = TaggableManager()
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_details', kwargs={'slug': self.slug})

    @property
    def comment_count(self):
        return Comment.objects.filter(blog=self).count()



class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=90)
    body = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name