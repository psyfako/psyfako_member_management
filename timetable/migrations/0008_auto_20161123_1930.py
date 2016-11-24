# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 19:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0007_auto_20161123_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workgroup',
            name='moderation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moderation', to='psyfako_core.Member'),
        ),
        migrations.AlterField(
            model_name='workgroup',
            name='protocol',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='protocol', to='psyfako_core.Member'),
        ),
    ]
