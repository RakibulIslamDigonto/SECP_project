from django.shortcuts import render
from .models import Albums
# Create your views here.

def albumspage(request):
    albums = Albums.objects.all()
    context = {
        'albums':albums

    }
    return render(request, 'album/albums.html', context)