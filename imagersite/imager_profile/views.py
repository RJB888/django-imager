from django.shortcuts import render
from django.views.generic.edit import UpdateView
from imager_profile.models import ImagerProfile
from django.urls import reverse_lazy
import pdb
# from django.http import HttpResponse
# from django.template import loader

# Create your views here.


def my_proflie_view(request):
    """Return how many uploaded private/public images/albums."""
    profile = request.user.profile
    public_photos = []
    private_photos = []
    public_albums = []
    private_albums = []
    my_photos = request.user.profile.photos.all()
    my_albums = request.user.profile.album.all()
    for photo in my_photos:
        if photo.published == "PBL":
            public_photos.append(photo)
        else:
            private_photos.append(photo)
    for album in my_albums:
        if album.published == "PBL":
            public_albums.append(album)
        else:
            private_albums.append(album)
    return render(request, 'imagersite/profile.html',
                           {'pub_photos': public_photos,
                            'priv_photos': private_photos,
                            'pub_albums': public_albums,
                            'priv_albums': private_albums,
                            'profile': profile})


def other_profile_view(request, username):
    """."""
    from django.contrib.auth.models import User
    requested_user = None
    users = User.objects.all()
    for user in users:
        if user.username == username:
            requested_user = user
    if requested_user is None:
        return render(request, 'imagersite/404.html', {})
    """Return how many uploaded private/public images/albums."""
    profile = requested_user.profile
    public_photos = []
    private_photos = []
    public_albums = []
    private_albums = []
    my_photos = requested_user.profile.photos.all()
    my_albums = requested_user.profile.album.all()
    for photo in my_photos:
        if photo.published == "PBL":
            public_photos.append(photo)
        else:
            private_photos.append(photo)
    for album in my_albums:
        if album.published == "PBL":
            public_albums.append(album)
        else:
            private_albums.append(album)
    return render(request, 'imagersite/other_profile.html',
                           {'pub_photos': public_photos,
                            'priv_photos': private_photos,
                            'pub_albums': public_albums,
                            'priv_albums': private_albums,
                            'profile': profile})


class UpdateProfileView(UpdateView):
    """View for updating a users profile."""
    template_name = "imagersite/update_profile.html"
    model = ImagerProfile
    fields = ["STYLE_CHOICES", "SERVICES_CHOICES", "website", "location",
              "bio", "phone", "fee", "services", "photo_styles"]
    success_url = reverse_lazy('my_profile')
