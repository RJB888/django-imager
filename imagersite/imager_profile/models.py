"""."""
from django.db import models
from django.contrib.auth.models import User


class ActiveProfileManager(models.Manager):
    """."""

    def get_queryset(self):
        """."""
        return super(ActiveProfileManager,
                     self).get_queryset().filter(user__is_active=True)


class ImagerProfile(models.Model):
    """."""

    STYLE_CHOICES = (['BW', 'black and white'],
                     ['PT', 'portrait'],
                     ['FAM', 'family'])
    SERVICES_CHOICES = (['WD', 'Weddings'],
                        ['SCH', 'School Photos'],
                        ['CEL', 'Celebrations'])
    website = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    bio = models.CharField(max_lenght=500)
    phone = models.CharField(max_lenght=10)
    fee = models.FloatField()
    active = ActiveProfileManager()
    services = models.CharField(choices=SERVICES_CHOICES)
    photo_styles = models.CharField(choices=STYLE_CHOICES)
    user = models.OneToOneField(User, related_name='profile',
                                on_delete=models.CASCADE)

    @property
    def is_active(self):
        """."""
        return self.user.is_active
