"""."""


from django.test import TestCase
import os
from django.contrib.auth.models import User
import factory
from imagersite.settings import BASE_DIR
from .models import Photo, Album
from imager_images.models import ImagerProfile
from django.test import Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse_lazy

import pdb

# Create your tests here.


class UserFactory(factory.django.DjangoModelFactory):
    """."""

    class Meta:
        """docstring for Meta."""

        model = User


class ProfileFactory(factory.django.DjangoModelFactory):
    """."""

    class Meta:
        """docstring for Meta."""

        model = ImagerProfile


class PhotoFactory(factory.django.DjangoModelFactory):
    """."""

    class Meta:
        """."""

        model = Photo


class AlbumFactory(factory.django.DjangoModelFactory):
    """."""

    class Meta:
        """."""

        model = Album


class ImagesTestCase(TestCase):
    """."""

    def setUp(self):
        """Make object."""
        print('this ran')
        user1 = UserFactory.create(username="Bob", first_name='Bob', last_name='Boberts')
        profile1 = ProfileFactory.create(user=user1, website='test', location='here', bio='isuck', phone='phone', fee=10, services='WD', photo_styles='BW')
        user2 = UserFactory.create(username="Jim")
        profile2 = ProfileFactory.create(user=user2, website='google', location='here', bio='isuck', phone='phone', fee=10, services='WD', photo_styles='BW')
        photo1 = PhotoFactory.create(title='title', description='Elephant', published='PBL', user=profile1, image='https://i.vimeocdn.com/portrait/58832_300x300')

        photo2 = PhotoFactory.create(title='White Elephant', description='in the room', published='PVT', user=profile1, image='https://pixabay.com/p-361514/?no_redirect')
        photo3 = PhotoFactory.create(title='Jims Photo', description='by jim', published='PBL', user=profile2, image='https://hiset.ets.org/rsc/img/icons/icon-tt-checklist.svg')
        album1 = AlbumFactory(title="First", description='who cares',
                              published="PBL", user=profile1)
        album1.photo.add(photo1)
        album2 = AlbumFactory(title="Second", description='im private',
                              published="PVT", user=profile1)
        album2.photo.add(photo2)

    def test_sample_test(self):
        """Debugging."""
        pdb.set_trace()
        self.assertTrue(True)

    # def test_setup(self):
    #     """."""
    #     self.assertTrue(User.objects.count() == 2)

    # def test_photos_are_created(self):
    #     """."""
    #     self.assertTrue(Photo.objects.count() == 3)

    # def test_albums_are_created(self):
    #     """."""
    #     self.assertTrue(Album.objects.count() == 2)

    # def test_album1_photo(self):
    #     """."""
    #     self.assertTrue(Album.objects.get(title='First').photo.get(title="title"))

#     def test_individual_photos_route(self):
#         """Test the detail view for a photo view shows url for image."""
#         number = Photo.objects.get(title='title').id
#         c = Client()
#         url = '/images/photos/' + str(number)
#         response = c.get(url)
#         self.assertTrue(b'title' in response.content)

#     def test_individual_photos_route2(self):
#         """Test the detail view for a photo shows first and last name."""
#         number = Photo.objects.get(title='title').id
#         c = Client()
#         url = '/images/photos/' + str(number)
#         response = c.get(url)
#         self.assertTrue(b'Bob Boberts' in response.content)

#     def test_individual_photos_route3(self):
#         """Test the detail view for a photo shows title of image."""
#         number = Photo.objects.get(title='title').id
#         c = Client()
#         url = '/images/photos/' + str(number)
#         response = c.get(url)
#         self.assertTrue(b'title' in response.content)

#     def test_individual_photos_route4(self):
#         """Test the detail view for a photo shows description."""
#         number = Photo.objects.get(title='title').id
#         c = Client()
#         url = '/images/photos/' + str(number)
#         response = c.get(url)
#         self.assertTrue(b'Elephant' in response.content)

#     def test_gallery_view_shows_only_public_photos(self):
#         """Test the detail view for a photo shows description."""
#         c = Client()
#         url = '/images/photos/'
#         response = c.get(url)
#         self.assertTrue(len(response.context['display_photos']) == 2)

#     def test_gallery_view_shows_multiple_users_photos(self):
#         """Test the detail view for a photo shows description."""
#         c = Client()
#         url = '/images/photos/'
#         response = c.get(url)
#         for photo in response.context['display_photos']:
#             self.assertTrue(photo.published == "PBL")

#     def test_album_gallery_only_shows_public(self):
#         """Ablum view for all album only shows public."""
#         c = Client()
#         url = '/images/albums/'
#         response = c.get(url)
#         self.assertTrue(b'First' in response.content)
#         self.assertTrue(b'Second' not in response.content)

#     def test_individual_album_response_200(self):
#         """Ablum view for all album only shows public."""
#         number = Album.objects.get(title='First').id
#         c = Client()
#         url = '/images/albums/' + str(number)
#         response = c.get(url)
#         self.assertTrue(response.status_code == 200)

#     def test_individual_album_shows_title(self):
#         """Ablum view for all album only shows public."""
#         number = Album.objects.get(title='First').id
#         c = Client()
#         url = '/images/albums/' + str(number)
#         response = c.get(url)
#         self.assertTrue(b"First" in response.content)

#     def test_post_to_create_photo(self):
#         """A post request to the add photo route should add it to db."""
#         file = open(os.path.join(BASE_DIR, 'MEDIA/images/dreams.jpg'), 'rb')
#         photo = SimpleUploadedFile('dreams.jpg', file.read())
#         user1 = ImagerProfile.active.first()
#         print('testt')
#         self.client.post(reverse_lazy('photo_form'),
#                          {'title': 'Whaddup',
#                           'description': 'I made this',
#                           'published': 'PBL',
#                           'user': user1.id,
#                           'image': photo})
#         output = Photo.objects.get(title='Whaddup')
#         self.assertTrue(output)

#     def test_post_new_photo_redirects_to_library(self):
#         """A post request to the add photo route should add it to db."""
#         file = open(os.path.join(BASE_DIR, 'MEDIA/images/dreams.jpg'), 'rb')
#         photo = SimpleUploadedFile('dreams.jpg', file.read())
#         user1 = ImagerProfile.active.first()
#         res = self.client.post(reverse_lazy('photo_form'),
#                                {'title': 'Whaddup',
#                                 'description': 'I made this',
#                                 'published': 'PBL',
#                                 'user': user1.id,
#                                 'image': photo})

#         self.assertTrue(res.url == '/images/library/')

#     def test_post_to_create_album(self):
#         """A post request to the add album route should add it to db."""
#         user1 = ImagerProfile.active.first()
#         print('testt')
#         self.client.post(reverse_lazy('album_form'),
#                          {'title': 'Thriller',
#                           'description': 'I made this',
#                           'published': 'PBL',
#                           'user': user1.id})
#         output = Album.objects.get(title='Thriller')
#         self.assertTrue(output)

#     def test_post_new_album_redirects_to_library(self):
#         """A post request to the add photo route should add it to db."""
#         user1 = ImagerProfile.active.first()
#         res = self.client.post(reverse_lazy('album_form'),
#                                {'title': 'Thriller',
#                                 'description': 'I made this',
#                                 'published': 'PBL',
#                                 'user': user1.id})

#         self.assertTrue(res.url == '/images/library/')

#     def test_post_to_update_photo(self):
#         """A post request to update photo route edits it in the db."""
#         file = open(os.path.join(BASE_DIR, 'MEDIA/images/dreams.jpg'), 'rb')
#         image = SimpleUploadedFile('dreams.jpg', file.read())
#         photo = Photo.objects.first()
#         user1 = ImagerProfile.active.first()
#         self.client.post(reverse_lazy('edit_photo', kwargs={'pk': photo.id}),
#                          {'title': 'Bad',
#                           'description': 'changed',
#                           'published': 'PBL',
#                           'user': user1.id,
#                           'image': image})
#         self.assertTrue(Photo.objects.get(id=photo.id).title == "Bad")

#     def test_post_to_update_photo_redirects_to_library(self):
#         """A post request to update photo route edits it in the db."""
#         file = open(os.path.join(BASE_DIR, 'MEDIA/images/dreams.jpg'), 'rb')
#         image = SimpleUploadedFile('dreams.jpg', file.read())
#         photo = Photo.objects.first()
#         user1 = ImagerProfile.active.first()
#         res = self.client.post(reverse_lazy('edit_photo',
#                                kwargs={'pk': photo.id}),
#                                {'title': 'Bad',
#                                 'description': 'changed',
#                                 'published': 'PBL',
#                                 'user': user1.id,
#                                 'image': image})
#         self.assertTrue(res.url == '/images/library/')

#     def test_post_to_update_album(self):
#         """A post request to update photo route edits it in the db."""
#         album = Album.objects.first()
#         user1 = ImagerProfile.active.first()
#         self.client.post(reverse_lazy('edit_album', kwargs={'pk': album.id}),
#                          {'title': 'Bad',
#                           'description': 'changed',
#                           'published': 'PBL',
#                           'user': user1.id})
#         self.assertTrue(Album.objects.get(id=album.id).title == "Bad")

#     def test_post_to_update_album_redirects_to_library(self):
#         """A post request to update photo route edits it in the db."""
#         album = Album.objects.first()
#         user1 = ImagerProfile.active.first()
#         res = self.client.post(reverse_lazy('edit_album',
#                                kwargs={'pk': album.id}),
#                                {'title': 'Bad',
#                                 'description': 'changed',
#                                 'published': 'PBL',
#                                 'user': user1.id})
#         self.assertTrue(res.url == '/images/library/')


"""
Test that one user can have several photos
Test that each photo can only have one user
test photos have attributes
Test One album owned by one user
Test one user can own several albums
Test any photo can be in more than one album
Test user can designate cover photo
Test album can have more than one photo
Test album cannot have photos from different users.

"""
