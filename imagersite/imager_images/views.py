"""."""

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from imager_images.models import Photo, Album
from django.urls import reverse_lazy
from rest_framework.response import Response
from imager_images.serializers import PhotoSerializer
from rest_framework import status
from django.contrib.auth.models import User
from imager_profile.models import ImagerProfile
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import permission_classes

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


# def photo_list(request, username, format=None):
#     """List all photo objects associated with, one user."""
#     try:
#         my_user = User.objects.get(username=username)
#         my_profile = ImagerProfile.active.get(user=my_user)
#         users_photos = Photo.objects.filter(user=my_profile)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = PhotoSerializer(users_photos, many=True)
#         return Response(serializer.data)

@permission_classes((permissions.IsAuthenticated, ))
class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def list(self, request, username):
        my_user = User.objects.get(username=username)
        my_profile = ImagerProfile.active.get(user=my_user)
        users_photos = Photo.objects.filter(user=my_profile)
        serializer = PhotoSerializer(users_photos, many=True)
        return Response(serializer.data)
