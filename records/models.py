# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.cache import cache
from management.models import NIPPILog
import recordUtils
from datetime import datetime, timedelta
from nips.models import Nip
import json
import os
import pprint
from memcached_stats import MemcachedStats
import memcache
import pytz
from django.utils import timezone

SECONDS_IN_DAY = 86400



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

        log_path = os.path.join(os.path.join(self.record_directory, "tmp"), "%s.json" % data_dict["time"])

        if os.path.isfile(log_path):

            raise OSError("File already exists.")
        
        else:
        
            with open(log_path, "w") as temp_file:
                json.dump(data_dict["data"], temp_file)



    def get_relevant_keys(self):

        cache_stats = MemcachedStats("127.0.0.1", 8001)
        all_keys = cache_stats.keys()

        relevant_keys = [key.replace(":1:", "") for key in all_keys if key.split("|")[0].replace(":1:", "") == str(self.pk)]

        return relevant_keys


    def cache_data(self, data_dict):

        cache_uid = "%s|%s" % (self.pk, data_dict["time"].replace(" ", "_"))
        cache.set(cache_uid, json.dumps(data_dict), SECONDS_IN_DAY)


    def get_todays_data(self):

        relevant_keys = self.get_relevant_keys()

        output = {"data": []}

        for key in relevant_keys:

            cached_data_point = json.loads(cache.get(key))

            data_point = {
                "datetime": cached_data_point["time"],
            }

            for k, v, in cached_data_point["data"].iteritems():
                data_point[k] = v

            output["data"].append(data_point)
        
        return output



    def get_archived_data(self, start_datetime, end_datetime):

        output = {"data": []}

        for record_file in os.listdir(self.record_directory):
            
            if record_file[-5:] == ".json":

                file_datetime_string = record_file.replace(".json", "")

                file_datetime = datetime.strptime(file_datetime_string, "%Y-%m-%d")

                if file_datetime.date() >= start_datetime.date() and file_datetime.date() <= end_datetime.date():

                    with open(os.path.join(self.record_directory, file_datetime_string + ".json")) as j_file:
                        loaded_json = json.load(j_file)

                    for data_point in loaded_json["data"]:
                        
                        if datetime.strptime(data_point["datetime"], "%Y-%m-%d %H:%M:%S") <= end_datetime:

                            output["data"].append(data_point)


        return output



    def get_records_in_range(self, start_datetime, end_datetime):

        
        temp_directory = os.path.join(self.record_directory, "tmp")



        if end_datetime.date() == datetime.today().date() and start_datetime.date() == datetime.today().date():
            
            output = {"data": []}

            keys = self.get_relevant_keys()

            for key in keys:
                
                string_datetime = key.split("|")[1].replace("_", " ")    
                key_datetime = datetime.strptime(string_datetime, "%Y-%m-%d %H:%M:%S")

                if key_datetime >= start_datetime and key_datetime <= end_datetime:

                    cached_data_point = json.loads(cache.get(key))
                    data_point = {"datetime": string_datetime}

                    for k, v, in cached_data_point.iteritems():
                        data_point[k] = v
                
                    output["data"].append(data_point)
        


        elif end_datetime.date() == datetime.today().date() and start_datetime.date() != datetime.today().date():
            
            output = self.get_todays_data()

            archive_output = self.get_archived_data(start_datetime, end_datetime)
            output["data"] += archive_output["data"]
        
        else:

            output = self.get_archived_data(start_datetime, end_datetime)

        return output

            

    def get_past_24_hours(self):

        now = datetime.now()
        this_time_yesterday = now - timedelta(days = 1)

        return self.get_records_in_range(this_time_yesterday, now)

    

    def get_past_week(self):
        
        now = datetime.now()
        this_time_a_week_ago = now - timedelta(days = 7)
        
        return self.get_records_in_range(this_time_a_week_ago, now)
    


    def get_past_hour(self):

        now = datetime.now()
        this_time_a_week_ago = now - timedelta(hours = 1)
        
        return self.get_records_in_range(this_time_a_week_ago, now)
    


    def get_past_quarter_hour(self):

        now = datetime.now()
        quarter_hour_ago = now - timedelta(minutes = 15)
        
        return self.get_records_in_range(quarter_hour_ago, now)



    def get_all_archived_data(self):

        output = {"data": []}

        for record_file in os.listdir(self.record_directory):
            
            if record_file[-5:] == ".json":

                with open(os.path.join(self.record_directory, record_file)) as j_file:
                    loaded_json = json.load(j_file)

                    output["data"] += loaded_json["data"]

        return output



    def get_all_data(self):

        output = {"data": []}

        todays_data = self.get_todays_data()
        archived_data = self.get_all_archived_data()

        output["data"] += todays_data["data"]
        output["data"] += archived_data["data"]

        return output



    def clear_temp_data(self):

        temp_directory = os.path.join(self.record_directory, "tmp")

        for temp_file in os.listdir(temp_directory):
            os.remove(os.path.join(temp_directory, temp_file))



    def write_to_archive(self, data, date_string):

        with open(os.path.join(self.record_directory, "%s.json" % date_string), "w") as j_file:
            json.dump(data, j_file)
        


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