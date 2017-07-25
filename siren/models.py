from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

from nips.models import Nip


class Siren(models.Model):

    SIREN_STATUS_OPTIONS = (
        ("D", "Dormant"),
        ("A", "Alert"),
    )

    nip = models.ForeignKey(Nip, null = True)
    name = models.CharField(max_length = 30, default = "")
    monitor_variable = models.CharField(max_length = 30, default = "temperature")
    acceptable_bounds_upper_limit = models.FloatField(default = 0.0)
    acceptable_bounds_lower_limit = models.FloatField(default = 0.0)
    message = models.CharField(max_length = 100, default = "Monitored variable out of bounds.")
    tolerance = models.IntegerField(default = 3)
    circular_buffer = models.CharField(max_length = 30, default = "")
    status = models.CharField(max_length = 1, choices = SIREN_STATUS_OPTIONS, default = "D")
    number_of_issues = models.IntegerField(default = 0)


    
    def alert_subscribers(self, message):
        
        for sub in self.subscription_set.all():

            pass



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





class Subscription(models.Model):

    siren = models.ForeignKey(Siren, null = True)
    user = models.ForeignKey(User, null = True)
    email_notification = models.BooleanField(default = True)
    text_notification = models.BooleanField(default = False)