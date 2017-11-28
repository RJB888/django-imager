from django.shortcuts import render

import pdb
# from django.http import HttpResponse
# from django.template import loader

# Create your views here.


def proflie_view(request):
    """Return how many uploaded private/public images/albums."""
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
    # pdb.set_trace()
    return render(request, 'imagersite/profile.html',
                           {'pub_photos': public_photos,
                            'priv_photos': private_photos,
                            'pub_albums': public_albums,
                            'priv_albums': private_albums})
