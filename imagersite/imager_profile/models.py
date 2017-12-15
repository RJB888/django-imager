"""."""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ActiveProfileManager(models.Manager):
    """."""

    def get_queryset(self):
        """."""
        return super(ActiveProfileManager,
                     self).get_queryset().filter(user__is_active=True)


class ImagerProfile(models.Model):
    """."""

    user = models.OneToOneField(User,
                                related_name='profile',
                                on_delete=models.CASCADE)

    STYLE_CHOICES = (['BW', 'black and white'],
                     ['PT', 'portrait'],
                     ['FAM', 'family'])
    SERVICES_CHOICES = (['WD', 'Weddings'],
                        ['SCH', 'School Photos'],
                        ['CEL', 'Celebrations'])
    website = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=50, null=True)
    bio = models.CharField(max_length=500, null=True)
    phone = models.CharField(max_length=10, null=True)
    fee = models.FloatField(null=True)
    active = ActiveProfileManager()
    services = models.CharField(max_length=30, choices=SERVICES_CHOICES, null=True)
    photo_styles = models.CharField(max_length=30, choices=STYLE_CHOICES, null=True)

    @property
    def is_active(self):
        """."""
        return self.user.is_active

    def __str__(self):
        """."""
        return self.user.username

    @receiver(post_save, sender=User)
    def attach_profile(instance, **kwargs):
        if kwargs['created']:
            profile = ImagerProfile(
                user=instance,
            )
            profile.save()
