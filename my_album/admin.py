from django.contrib import admin
from .models import Albums
# Register your models here.

class AlbumsAdmin(admin.ModelAdmin):

    list_display = [
        'thumbnail',
        'discription',
        'creation'
    ]

admin.site.register(Albums, AlbumsAdmin)

