# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nips', '0004_auto_20170725_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nip',
            name='status',
            field=models.CharField(choices=[('AA', 'Awaiting Activation'), ('W', 'Working'), ('D', 'Disabled'), ('E', 'Error'), ('S', 'Siren Active')], default='AA', max_length=2),
        ),
    ]