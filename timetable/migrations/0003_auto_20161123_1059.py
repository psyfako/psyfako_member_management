# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 10:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20161122_2221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slot',
            old_name='slot_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='slot',
            old_name='slot_short_name',
            new_name='short_name',
        ),
    ]
