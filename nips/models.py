# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class NipLocation(models.Model):

    name = models.CharField(max_length = 30, unique = True)


class Nip(models.Model):

    NIP_STATUS_OPTIONS = (
        ("AA", "Awaiting Activation"),
        ("W", "Working"),
        ("D", "Disabled"),
        ("E", "Error"),
    )

    location = models.ForeignKey(NipLocation, null = True)
    name = models.CharField(max_length = 20, unique = True)
    uid = models.CharField(max_length = 50, unique = True, blank = True, default = "")
    status = models.CharField(max_length = 2, choices = NIP_STATUS_OPTIONS, default = "AA")

    def generate_uid(self):
        self.uid = "%d_%s" % (self.pk, self.name)
        self.save()