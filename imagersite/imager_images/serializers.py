from rest_framework import serializers
from imager_images.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'title', 'description', 'date_uploaded',
                  'date_modified', 'date_published', 'published',
                  'user', 'image')

    def create(self, validated_data):
        """Create and return a new `Photo` instance, given the validated data."""
        return Photo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing `Photo` instance, given the validated data."""
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.date_uploaded = validated_data.get('date_uploaded', instance.date_uploaded)
        instance.date_modified = validated_data.get('date_modified', instance.date_modified)
        instance.date_published = validated_data.get('date_published', instance.date_published)
        instance.published = validated_data.get('published', instance.published)
        instance.user = validated_data.get('user', instance.user)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
