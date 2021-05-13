from django.db import models

# Create your models here.

class Albums(models.Model):
    thumbnail = models.ImageField(upload_to = 'album/images/')
    discription = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)
