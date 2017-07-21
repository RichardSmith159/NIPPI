# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nip',
            name='uid',
            field=models.CharField(blank=True, default='', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='nip',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='niplocation',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]