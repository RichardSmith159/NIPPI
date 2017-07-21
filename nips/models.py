# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class NipLocation(models.Model):

    name = models.CharField(max_length = 30, unique = True)


class Nip(models.Model):

    location = models.ForeignKey(NipLocation, null = True)
    name = models.CharField(max_length = 20, unique = True)
    uid = models.CharField(max_length = 50, unique = True, blank = True, default = "")

    def generate_uid(self):
        self.uid = "%d_%s" % (self.pk, self.name)
        self.save()