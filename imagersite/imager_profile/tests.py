"""."""


from django.test import TestCase
from django.contrib.auth.models import User
from .models import ImagerProfile

# Create your tests here.


class ProfileTestCase(TestCase):
    """."""

    def test_imager_profile_class(self):
        """."""
        User.objects.create(username='Bob')
        user1 = User.objects.get(username='Bob')
        profile = ImagerProfile.active.get(user=user1)
        profile.location = 'here'
        self.assertEqual(profile.user.username, "Bob")
        self.assertEqual(profile.location, "here")

    def test_user_is_active(self):
        """."""
        User.objects.create(username='Bob')
        user1 = User.objects.get(username='Bob')
        User.objects.create(username='Joe')
        user2 = User.objects.get(username='Joe')
        profile = ImagerProfile.active.get(user=user1)
        profile2 = ImagerProfile.active.get(user=user2)

        self.assertEqual(profile.is_active, True)
        self.assertEqual(profile2.is_active, True)
