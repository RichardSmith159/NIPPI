# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siren', '0003_siren_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='siren',
            name='circular_buffer',
            field=models.CharField(default='', max_length=30),
        ),
    ]
