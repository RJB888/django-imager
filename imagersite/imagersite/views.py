"""."""


from django.shortcuts import render
from django.views.generic.list import ListView
from imager_images.models import Photo, Album
from django.core.paginator import Paginator, PageNotAnInteger
import random

# Create your views here.


def home_view(request):
    """."""
    photos = Photo.objects.all()
    published = []
    for photo in photos:
        if photo.published == "PBL":
            published.append(photo)
    carousel_list = []
    if len(published) >= 3:
        while len(carousel_list) < 3:
            index = random.randint(0, len(published) - 1)
            image = published[index]
            if image not in carousel_list:
                carousel_list.append(image)
    else:
        for image in published:
            carousel_list.append(image)
    return render(request, 'imagersite/home.html', {'images': carousel_list})


class LibraryView(ListView):
    """."""

    template_name = 'imagersite/library.html'
    model = Album
    paginate_by = 4

    def get_context_data(self, **kwargs):
        """."""
        context = super(LibraryView, self).get_context_data(**kwargs)
        users_photos = Photo.objects.filter(user=self.request.user.profile)
        users_albums = Album.objects.filter(user=self.request.user.profile)
        context['users_photos'] = users_photos
        context['users_albums'] = users_albums
        photo_paginator = Paginator(users_photos, 4)
        album_paginator = Paginator(users_albums, 4)
        photo_page = self.request.GET.get('photo_page')
        try:
            display_photos = photo_paginator.page(photo_page)
        except PageNotAnInteger:
            display_photos = photo_paginator.page(1)
        context['display_photos'] = display_photos
        album_page = self.request.GET.get('album_page')
        try:
            display_albums = album_paginator.page(album_page)
        except PageNotAnInteger:
            display_albums = album_paginator.page(1)
        context['display_albums'] = display_albums
        return context
