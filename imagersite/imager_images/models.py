"""Main Docstring Goes Here."""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

PUBLISHED_CHOICES = (
    ['PVT', 'private'],
    ['SH', 'shared'],
    ['PBL', 'public'])


class Photo(models.Model):
    """Do some modeling."""

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=120)
    date_uploaded = models.DateField()
    date_modified = models.DateField()
    date_published = models.DateField()
    published = models.CharField(max_length=15, choices=PUBLISHED_CHOICES)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Album(models.Model):
    """Do some albuming."""

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=120)
    date_uploaded = models.DateField()
    date_modified = models.DateField()
    date_published = models.DateField()
    published = models.CharField(max_length=15, choices=PUBLISHED_CHOICES)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ManyToManyField(Photo)
    cover = models.OneToOneField(Photo, related_name='+')
