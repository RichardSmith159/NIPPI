# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 11:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siren', '0007_auto_20170726_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='siren',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='siren_subscription', to='siren.Siren'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscribed_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
