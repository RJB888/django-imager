"""imagersite URL Configuration."""

from django.conf.urls import url, include
from django.contrib import admin
from imagersite import views, settings
from django.contrib.auth import views as log_views
from imager_profile.views import my_proflie_view, other_profile_view, UpdateProfileView, UpdateUserView
from django.conf.urls.static import static
from imager_images import views as image_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_view, name='homepage'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^login/', log_views.login),
    url(r'^profile/edit/(?P<pk>\d+)', UpdateProfileView.as_view(), name="update_profile"),
    url(r'^profile/(\w+)', other_profile_view, name='other_profile'),
    url(r'^profile/', my_proflie_view, name='my_profile'),
    url(r'^images/library/', views.LibraryView.as_view(), name="library"),
    url(r'^images/photos/add/', image_views.CreatePhotoView.as_view(),
        name="photo_form"),
    url(r'^images/photos/(?P<pk>\d+)/edit/',
        image_views.EditPhotoView.as_view(),
        name="edit_photo"),
    url(r'^images/albums/add/', image_views.CreateAlbumView.as_view(),
        name="album_form"),
    url(r'^images/albums/(?P<pk>\d+)/edit/',
        image_views.EditAlbumView.as_view(),
        name="edit_album"),
    url(r'^images/photos/(?P<pk>\d+)$',
        image_views.IndividualPhotoView.as_view(),
        name="individual_photos"),
    url(r'^images/photos/$', image_views.PublishedPhotoView.as_view(),
        name="public_photos"),
    url(r'^images/albums/(?P<pk>\d+)$',
        image_views.IndividualAlbumView.as_view(),
        name="individual_album"),
    url(r'^images/albums/$', image_views.PublishedAlbumView.as_view(),
        name="public_album"),
    url(r'^images/users/(?P<pk>\d+)', UpdateUserView.as_view(),
        name="update_user"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL)

# comment to push
