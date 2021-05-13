from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to = 'blog/images/')
    short_discription = models.TextField()
    discription = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)