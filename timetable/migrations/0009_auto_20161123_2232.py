# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 22:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0008_auto_20161123_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workgroup',
            name='room',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.Room'),
        ),
    ]
