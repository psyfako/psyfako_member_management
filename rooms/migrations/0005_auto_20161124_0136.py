# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-24 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20161123_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='lat',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='building',
            name='lng',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
