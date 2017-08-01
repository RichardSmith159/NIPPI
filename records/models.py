# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.cache import cache
from management.models import NIPPILog
import recordUtils
from datetime import datetime
from nips.models import Nip
import json
import os
import pprint


class NipRecord(models.Model):

    nip = models.ForeignKey(Nip, null = True)
    record_directory = models.CharField(max_length = 20, default = "")

    def setup(self):
        
        record_directory = "records/archive/%s" % str(self.pk)

        try:

            os.mkdir(record_directory)
            os.makedirs(os.path.join(record_directory, "tmp"))
        
        except OSError as e:

            NIPPILog.objects.create(
                log_type = "E",
                details = "Could not create nip records directory: DIRECTORY '%s' ALREADY EXISTS" % record_directory
            )
        
        else:

            self.record_directory = record_directory
            self.save()



    def log_data(self, data_dict):
        
        date = datetime.strptime(data_dict["time"], '%Y-%m-%d %H:%M:%S.%f').date()

        log_path = os.path.join(os.path.join(self.record_directory, "tmp"), "%s.json" % data_dict["time"])

        if os.path.isfile(log_path):

            raise OSError("File already exists.")
        
        else:
        
            with open(log_path, "w") as temp_file:
                json.dump(data_dict["data"], temp_file)



    def cache_data(self, data_dict):

        cache_uid = "%s|%s" % (self.nip.pk, data_dict["time"].replace(" ", "_"))
        print "CUID:", cache_uid
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

    def clear_temp_data(self):

        temp_directory = os.path.join(self.record_directory, "tmp")

        for temp_file in os.listdir(temp_directory):

            os.remove(os.path.join(temp_directory, temp_file))

        
    
    def collate_temp_data(self):

        output_data = {"data": []}

        temp_directory = os.path.join(self.record_directory, "tmp")

        for temp_file in os.listdir(temp_directory):

            file_datetime_string = temp_file.replace(".json", "")

            data_point = {"datetime": file_datetime_string.split(".")[0]}

            with open(os.path.join(temp_directory, temp_file)) as j_file:
                
                loaded_data = json.load(j_file)

                for k, v in loaded_data.iteritems():

                    data_point[k] = v

            output_data["data"].append(data_point)
            
        return output_data