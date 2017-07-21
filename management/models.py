# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import datetime

class NIPPILog(models.Model):

    LOG_TYPES = (
        ("E", "ERROR"),
        ("I", "INFO"),
        ("A", "ACTIVITY"),
    )

    log_type = models.CharField(max_length = 1, choices = LOG_TYPES, default = "I")
    details = models.CharField(max_length = 100, default = "")
    datetime = models.DateTimeField(default = datetime.datetime.now)


class UserDetails(models.Model):

    user = models.OneToOneField(User)
    name = models.CharField(max_length = 50)
    contact_number = models.CharField(max_length = 20)