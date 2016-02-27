# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('type', models.CharField(choices=[('bootstrap', 'bootstrap')], max_length=20)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('started', 'started'), ('finished', 'finished'), ('failed', 'failed')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fqdn', models.CharField(max_length=100)),
                ('client_rb_path', models.CharField(blank=True, max_length=100)),
                ('key_path', models.CharField(blank=True, max_length=100)),
                ('result', models.TextField(blank=True)),
            ],
        ),
    ]
