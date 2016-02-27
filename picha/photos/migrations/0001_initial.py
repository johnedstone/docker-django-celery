# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_on', models.DateTimeField(verbose_name='Created on', auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('link', models.URLField(help_text='The URL to the image page', verbose_name='Photo Link', max_length=255)),
                ('image_url', models.URLField(help_text='The URL to the image file itself', verbose_name='Image URL', max_length=255)),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'Photos',
                'verbose_name': 'Photo',
                'ordering': ['-created_on', 'title'],
            },
        ),
    ]
