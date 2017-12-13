"""."""

from django.test import Client
from django.test import TestCase
from django.core import mail
from django.contrib.auth.models import User
from imager_images.models import Photo, Album
from imager_profile.models import ImagerProfile
import factory
import pdb


class ProfileTestCase(TestCase):
    """."""

    def test_home_route_response_200(self):
        """."""
        c = Client()
        response = c.get('/')
        self.assertTrue(response.status_code == 200)

    def test_login_route_response_200(self):
        """."""
        c = Client()
        response = c.get('/accounts/login/')
        self.assertTrue(response.status_code == 200)

    def test_register_route_response_200(self):
        """."""
        c = Client()
        response = c.get('/accounts/register/')
        self.assertTrue(response.status_code == 200)

    def test_mailbox_empty(self):
        """."""
        self.assertEqual(len(mail.outbox), 0)

    def test_register_post_new_account_redirects(self):
        """."""
        c = Client()
        response = c.post('/accounts/register', {'username': 'test1',
                                                 'email': 'test@test.com',
                                                 'password1': 'UltraTest',
                                                 'password2': 'UltraTest'}, follow=True)
        self.assertTrue(response.status_code == 200)

    def test_homepage_has_photos_in_db(self):
        """Homepage shows photos when they exist in database."""
        User.objects.create(username='Bob')
        user1 = User.objects.get(username='Bob')
        profile1 = ImagerProfile.active.get(user=user1)
        Photo.objects.create(title='title', description=' ', published='PBL', user=profile1, image='https://i.vimeocdn.com/portrait/58832_300x300')
        c = Client()
        response = c.get('/')
        self.assertTrue(b"/media/https%3A/i.vimeocdn.com/portrait/58832_300x300" in response.content)

    def test_homepage_has_placeholder_no_images_in_db(self):
        """Homepage shows placeholder images when no images in database."""
        c = Client()
        response = c.get('/')
        self.assertTrue(b"http://placehold.it/900x350" in response.content)
