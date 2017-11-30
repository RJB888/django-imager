from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from imager_images.models import Photo, Album

# Create your views here.


class PublishedPhotoView(ListView):
    """."""

    template_name = 'imagersite/public_photos.html'
    model = Photo

    def get_context_data(self, **kwargs):
        """."""
        context = super(PublishedPhotoView, self).get_context_data(**kwargs)
        context['display_photos'] = Photo.objects.filter(published="PBL").all()
        # import pdb; pdb.set_trace()
        return context


class IndividualPhotoView(DetailView):
    """."""

    template_name = 'imagersite/individual_photo.html'
    model = Photo

    def get_context_data(self, **kwargs):
        """."""
        context = super(IndividualPhotoView, self).get_context_data(**kwargs)
        import pdb; pdb.set_trace()
        # context['display_photos'] = Photo.objects.filter(published="PBL").all()
        # import pdb; pdb.set_trace()
        return context
