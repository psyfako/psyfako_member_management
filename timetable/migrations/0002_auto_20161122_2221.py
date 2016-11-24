# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-22 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='slot_short_name',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AddField(
            model_name='workgroup',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
