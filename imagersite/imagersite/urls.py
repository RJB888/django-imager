"""imagersite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from imagersite import views, settings
from django.contrib.auth import views as log_views
from imager_profile.views import my_proflie_view, other_profile_view
from django.conf.urls.static import static
from imager_images.views import PublishedPhotoView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_view, name='homepage'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^login/', log_views.login),
    url(r'^profile/(\w+)', other_profile_view, name='other_profile'),
    url(r'^profile/', my_proflie_view, name='my_profile'),
    url(r'^images/library/', views.LibraryView.as_view(), name="library"),
    url(r'^images/photos/', PublishedPhotoView.as_view(), name="public_photos")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL)
