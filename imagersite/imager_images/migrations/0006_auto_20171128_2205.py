# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-28 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0005_auto_20171128_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='photo',
            field=models.ManyToManyField(blank=True, related_name='album', to='imager_images.Photo'),
        ),
        migrations.AlterField(
            model_name='album',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='imager_profile.ImagerProfile'),
        ),
    ]
