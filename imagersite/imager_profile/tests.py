"""."""


from django.test import TestCase
from django.contrib.auth.models import User
from .models import ImagerProfile

# Create your tests here.


class ProfileTestCase(TestCase):
    """."""

    def setup(self):
        bob = User()
        bob.username = "Joe"
        bob_profile = ImagerProfile()
        bob_profile.user = bob
        bob = User()
        bob_profile.website = "James.com"
        jim.username = "Jeff"
        jim_profile = ImagerProfile()
        jim_profile.user = jim
        profile1 = ImagerProfile.active.create()

    def test_imager_profile_class(self):
        """."""
        profile = ImagerProfile.active.get(website="James.com")
        self.assertEqual(profile.user.username, "Joe")

    def test_user_is_active(self):
        """."""
        profile = ImagerProfile.active.get(website="James.com")

        self.assertEqual(profile.is_active, True)
