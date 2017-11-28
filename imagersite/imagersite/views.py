from django.shortcuts import render
from imager_images.models import Photo
import pdb

# Create your views here.


def home_view(request):
    """."""
    photos = Photo.objects.get()
    return render(request, 'imagersite/base.html', {'images': photos})
