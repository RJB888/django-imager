"""."""

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from imager_images.models import Photo, Album
from django.urls import reverse_lazy

# Create your views here.


class PublishedPhotoView(ListView):
    """."""

    template_name = 'imagersite/public_photos.html'
    model = Photo

    def get_context_data(self, **kwargs):
        """."""
        context = super(PublishedPhotoView, self).get_context_data(**kwargs)
        context['display_photos'] = Photo.objects.filter(published="PBL").all()
        return context


class IndividualPhotoView(DetailView):
    """."""

    template_name = 'imagersite/individual_photo.html'
    model = Photo

    def get_context_data(self, **kwargs):
        """."""
        context = super(IndividualPhotoView, self).get_context_data(**kwargs)
        return context


class PublishedAlbumView(ListView):
    """."""

    template_name = 'imagersite/public_albums.html'
    model = Album

    def get_context_data(self, **kwargs):
        """."""
        context = super(PublishedAlbumView, self).get_context_data(**kwargs)
        context['display_albums'] = Album.objects.filter(published="PBL").all()
        # import pdb; pdb.set_trace()
        return context


class IndividualAlbumView(DetailView):
    """."""

    template_name = 'imagersite/individual_album.html'
    model = Album

    def get_context_data(self, **kwargs):
        """."""
        context = super(IndividualAlbumView, self).get_context_data(**kwargs)
        return context


class CreatePhotoView(CreateView):
    """."""

    template_name = 'imager_images/create_photo.html'
    model = Photo

    fields = ['title', 'description', 'published', 'user', 'image']
    success_url = reverse_lazy('library')


class CreateAlbumView(CreateView):
    """."""

    template_name = 'imager_images/create_album.html'
    model = Album

    fields = ['title', 'description', 'published', 'user', 'photo', 'cover']
    success_url = reverse_lazy('library')
