# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 08:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siren', '0014_alert_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='seen_by',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
