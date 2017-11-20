from django.db import models
from django.contrib.auth.models import User

class ImagerProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    website = models.CharField(max_length=100)
