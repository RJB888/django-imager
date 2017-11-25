"""."""


from django.test import TestCase
from django.contrib.auth.models import User
import factory
from .models import Photo, Album

# Create your tests here.


class UserFactory(factory.django.DjangoModelFactory):
    """."""

    class Meta:
        """docstring for Meta."""

        model = User


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
        print("this ran")
        user1 = UserFactory.create(username="Bob")
        # user1.save()
        user2 = UserFactory.create(username="Jim")
        # user2.save()
        photo1 = PhotoFactory.create(title="birds",
                                     published="PVT",
                                     user=user1)

        photo2 = PhotoFactory.create(title="flowers",
                                     published="PBL",
                                     user=user1)

        album1 = AlbumFactory(title="First",
                              published="PVT",
                              user=user1,
                              cover=photo1
                              )
        album1.photo.add(photo1)
        # import pdb; pdb.set_trace()
        album2 = AlbumFactory(title="Second",
                              published="PVT",
                              user=user2,
                              cover=photo2
                              )
        # import pdb; pdb.set_trace()
        album2.photo.add(photo2)
        # album3 = AlbumFactory(title="Third",
        #                       published="PVT",
        #                       user=user2
        #                       )
        # album3.save()

    def test_setup(self):
        """."""
        self.assertTrue(User.objects.count() == 2)

    def test_photos_are_created(self):
        """."""
        self.assertTrue(Photo.objects.count() == 1)

    def test_albums_are_created(self):
        """."""
        self.assertTrue(Album.objects.count() == 1)

    def test_album1_photo(self):
        """."""
        self.assertTrue(Album.objects.get(title='First').photo.get(title="birds"))

    # def test_user_has_multiple_photos(self):
    #     """."""
    #     self.assertTrue(Photo.objects.get(id=2).user.username == "Bob")

    # def test_photo_model(self):
    #     pass
    # def test_album_model(self):
    #     pass

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
