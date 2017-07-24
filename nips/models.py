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
        ("T", "Outside Tolerance")
    )

    location = models.ForeignKey(NipLocation, null = True)
    name = models.CharField(max_length = 20, unique = True)
    uid = models.CharField(max_length = 50, unique = True, blank = True, default = "")
    status = models.CharField(max_length = 2, choices = NIP_STATUS_OPTIONS, default = "AA")

    def get_verbose_status(self):

        return self.get_status_display()

    def generate_uid(self):
        self.uid = "%d_%s" % (self.pk, self.name)
        self.save()

    
    def get_record(self):

        return self.record_set.all()[0]
