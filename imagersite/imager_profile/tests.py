"""."""


from django.test import TestCase
from django.contrib.auth.models import User
from .models import ImagerProfile

# Create your tests here.


class ProfileTestCase(TestCase):
    """."""

    def setup(self):
        pass

    def test_imager_profile_class(self):
        """."""
        User.objects.create(username='Bob')
        user1 = User.objects.get(username='Bob')
        ImagerProfile.active.create(user=user1, website='bob.com', location='here', bio='who', phone='phone', fee=10, services='WD', photo_styles='BW')

        User.objects.create(username='Joe')
        user2 = User.objects.get(username='Joe')
        ImagerProfile.active.create(user=user2, website='joe.com', location='there', bio='cares', phone='phone', fee=10, services='WD', photo_styles='BW')
        profile = ImagerProfile.active.get(website="bob.com")
        self.assertEqual(profile.user.username, "Bob")
        self.assertEqual(profile.location, "here")

    def test_user_is_active(self):
        """."""
        User.objects.create(username='Bob')
        user1 = User.objects.get(username='Bob')
        ImagerProfile.active.create(user=user1, website='bob.com', location='here', bio='who', phone='phone', fee=10, services='WD', photo_styles='BW')

        User.objects.create(username='Joe')
        user2 = User.objects.get(username='Joe')
        ImagerProfile.active.create(user=user2, website='joe.com', location='there', bio='cares', phone='phone', fee=10, services='WD', photo_styles='BW')
        profile = ImagerProfile.active.get(website="bob.com")
        profile = ImagerProfile.active.get(website="joe.com")

        self.assertEqual(profile.is_active, True)
