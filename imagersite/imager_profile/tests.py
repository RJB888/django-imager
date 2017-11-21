"""."""


from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.


class ProfileTestCase(TestCase):
    """."""

    def test_imager_profile_class(self):
        """."""
        from .models import ImagerProfile
        bob = User()
        bob.username = "Joe"
        bob_profile = ImagerProfile()
        bob_profile.user = bob
        self.assertEqual(bob_profile.user.username, "Joe")

    def test_user_is_active(self):
        """."""
        from .models import ImagerProfile
        bob = User()
        bob_profile = ImagerProfile()
        bob_profile.user = bob
        self.assertEqual(bob_profile.is_active, True)
