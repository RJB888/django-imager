"""."""

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from imager_images.models import Photo, Album
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from imager_images.models import Photo
from imager_images.serializers import PhotoSerializer

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

    # def post(self, *args, **kwargs):
    #     import pdb; pdb.set_trace()
    #     context = super(CreatePhotoView, self).post(**kwargs)
    #     return context


class EditPhotoView(UpdateView):
    """."""

    template_name = 'imager_images/edit_photo.html'
    model = Photo

    fields = ['title', 'description', 'published', 'user', 'image']
    success_url = reverse_lazy('library')
    print('and here')


class CreateAlbumView(CreateView):
    """."""

    template_name = 'imager_images/create_album.html'
    model = Album

    fields = ['title', 'description', 'published', 'user', 'photo', 'cover']
    success_url = reverse_lazy('library')
    print('and here')


class EditAlbumView(UpdateView):
    """."""

    template_name = 'imager_images/edit_album.html'
    model = Album

    fields = ['title', 'description', 'published', 'user', 'photo', 'cover']
    success_url = reverse_lazy('library')


def photo_list(request, username):
    """List all photo objects associated with one user."""
    if request.method == 'GET':
        photos = Photo.objects.all()
        users_photos = [photo for photo in photos if photo.user.user.username == username]
        # for photo in photos:
        #     if photo.user.username == username:
        #         users_photos.append(photo)
        serializer = PhotoSerializer(users_photos, many=True)
        return JsonResponse(serializer.data, safe=False)
