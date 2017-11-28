"""Main Docstring Goes Here."""

from django.db import models
from imager_profile.models import ImagerProfile

# Create your models here.

PUBLISHED_CHOICES = (
    ['PVT', 'private'],
    ['SH', 'shared'],
    ['PBL', 'public'])


class Photo(models.Model):
    """Do some modeling."""

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=120, blank=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now_add=True)  # should set this to auto pop when published is set to public
    published = models.CharField(max_length=15, choices=PUBLISHED_CHOICES)
    user = models.ForeignKey(ImagerProfile, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='images', null=True)


class Album(models.Model):
    """Do some albuming."""

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=120, blank=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now_add=True)
    published = models.CharField(max_length=15, choices=PUBLISHED_CHOICES)
    user = models.ForeignKey(ImagerProfile, on_delete=models.CASCADE, related_name='album')
    photo = models.ManyToManyField(Photo, blank=True, related_name='album')
    cover = models.ForeignKey(Photo, related_name='cover', blank=True)


# new stuff

# @receiver(post_save, sender=User)
# def create_profile(sender, **kwargs):
