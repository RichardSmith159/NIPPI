from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

from nips.models import Nip


class Siren(models.Model):

    nip = models.ForeignKey(Nip, null = True)
    name = models.CharField(max_length = 30, default = "")
    monitor_variable = models.CharField(max_length = 30, default = "temperature")
    acceptable_bounds_upper_limit = models.FloatField(default = 0.0)
    acceptable_bounds_lower_limit = models.FloatField(default = 0.0)
    message = models.CharField(max_length = 100, default = "Monitored variable out of bounds.")
    tolerance = models.IntegerField(default = 3)

    def check_data(self, data):
        pass
    
    def alert_subscribers(self):
        
        for sub in self.subscription_set.all():

            pass




class Subscription(models.Model):

    siren = models.ForeignKey(Siren, null = True)
    user = models.ForeignKey(User, null = True)
    email_notification = models.BooleanField(default = True)
    text_notification = models.BooleanField(default = False)