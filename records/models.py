# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from management.models import NIPPILog
import recordUtils
from datetime import datetime
from nips.models import Nip
import json
import os


class NipRecord(models.Model):

    nip = models.ForeignKey(Nip, null = True)
    record_directory = models.CharField(max_length = 20, default = "")

    def setup(self):
        
        record_directory = "records/archive/%s_%d" % (nip.name, nip.pk)

        try:

            os.mkdir(record_directory)
            os.mkdir(os.join(record_directory, "tmp"))
        
        except OSError as e:

            NIPPILog.objects.create(
                log_type = "E",
                details = "Could not create nip records directory: DIRECTORY '%s' ALREADY EXISTS" % record_directory
            )
        
        else:

            self.record_directory = record_directory
            self.save()



    def log_data(self, data_dict):
        
        log_path = os.join(self.record_directory, "%s.json" % data_dict["time"])

        if os.path.isfil(log_path):

            raise OSError("File already exists.")
        
        else:
        
            with open(log_path, "w") as temp_file:
                json.dump(data_dict["data"], temp_file)



    def cache_data(self, data_dict):
        
        cache_uid = "%s_%s" % (nip.uid, data_dict["time"])
        cache.set(cache_uid, json.dumps(data_dict["data"]))



    def get_records_in_range(self, start_datetime, end_datetime):
        pass

    def get_past_24_hours(self):
        pass
    
    def get_todays_data(self):

        midnight_today = recordUtils.get_midnight_for_date(datetime.now())
        data_dict = recordUtils.get_records_from_cache(self.nip.pk, self.nip.name)
    
    def get_past_week(self):
        pass
    
    def get_past_hour(self):
        pass
    
    def get_past_quarter_hour(self):
        pass