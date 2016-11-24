# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0005_workgroup_group_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workgroup',
            name='group_type',
            field=models.CharField(choices=[('O', 'Offen'), ('A', 'Austausch'), ('W', 'Arbeit'), ('P', 'Positionspapier')], max_length=1),
        ),
    ]