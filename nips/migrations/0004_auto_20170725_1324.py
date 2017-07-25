# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nips', '0003_nip_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nip',
            name='status',
            field=models.CharField(choices=[('AA', 'Awaiting Activation'), ('W', 'Working'), ('D', 'Disabled'), ('E', 'Error'), ('T', 'Outside Tolerance')], default='AA', max_length=2),
        ),
    ]
