from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

from nips.models import Nip
from datetime import datetime


class Siren(models.Model):

    SIREN_STATUS_OPTIONS = (
        ("D", "Dormant"),
        ("P", "Paused"),
        ("A", "Alert"),
    )

    nip = models.ForeignKey(Nip, null = True)
    name = models.CharField(max_length = 30, default = "")
    registered_users = models.ManyToManyField(User)
    creator = models.OneToOneField(User, null = True, related_name = "creator")
    status = models.CharField(max_length = 1, choices = SIREN_STATUS_OPTIONS, default = "D")
    monitor_variable = models.CharField(max_length = 30, default = "temperature")
    
    tolerance = models.IntegerField(default = 3)
    acceptable_bounds_upper_limit = models.FloatField(default = 0.0)
    acceptable_bounds_lower_limit = models.FloatField(default = 0.0)
    circular_buffer = models.CharField(max_length = 30, default = "")
    
    message = models.CharField(max_length = 100, default = "Monitored variable out of bounds.")

    email_notification = models.BooleanField(default = True)
    text_notification = models.BooleanField(default = False)

    def alert_users(self):
        pass

    def get_verbose_status(self):

        return self.get_status_display()

    def switch_off(self):

        self.status = "D"
        self.alert_subscribers(self.name + ": Alert Deactivated.")
        self.save()
    
    def check_data(self, data):

        num_out_of_tolerance = 0
        
        for point in data:
            if point < self.acceptable_bounds_lower_limit or point > self.acceptable_bounds_upper_limit:
                num_out_of_tolerance += 1
        
        if num_out_of_tolerance == self.tolerance:
            
            self.status = "A"
            self.alert_subscribers(self.message)
            self.save()

            self.nip.status = "T"
            self.nip.save()


    def shift_buffer(self, new_data_point):

        current_buffer = self.circular_buffer.replace("[", "").replace("]", "").split(",")

        last_index = len(current_buffer) - 1

        if len(current_buffer) == self.tolerance:

            current_buffer.pop(last_index)

            current_buffer.insert(0, new_data_point)
        
        else:

            current_buffer.insert(0, new_data_point)
        
        self.circular_buffer = str(current_buffer)
        self.save()


class Alert(models.Model):

    ALERT_STATUS_OPTIONS = (
        ("A", "Active"),
        ("S", "Seen"),
        ("H", "Handled")
    )

    siren = models.ForeignKey(Siren, null = True)
    status = models.CharField(max_length = 1, choices = ALERT_STATUS_OPTIONS, default = "A")
    alert_datetime = models.DateTimeField(default = datetime.now)
    handled_datetime = models.DateTimeField(null = True, blank = True)
    comments = models.CharField(max_length = 200, default = "")
    seen_by = models.ManyToManyField(User)
    handled_by = models.ForeignKey(User, null = True, related_name = "handled_by")

    def get_verbose_status(self):

        return self.get_status_display()