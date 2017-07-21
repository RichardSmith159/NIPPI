from django.core.cache import cache
from datetime import datetime
from memcached_stats import MemcachedStats
import json

# returns datetime corresponding to midnight for given datetime
def get_midnight_for_date(current_datetime):

    if not isinstance(current_datetime, datetime):

        return ValueError("current_datetime must be a datetime object.")

    else:

        return datetime.replace(hour = 0, minute = 0, second = 0, microsecond = 0)



def get_records_between_datetimes_from_filesystem(directory, start_datetime, end_datetime):
    pass



def get_nip_records_from_cache(nip_pk, nip_name):

    mem = MemcachedStats()

    nip_uid = "%d_%s" % (nip_pk, nip_name)

    relevant_keys = [key for key in mem.keys() if nip_uid in key]

    data = {}

    for key in relevant_keys:

        time = key.splt("_")[2]

        data[key] = json.loads(cache.get(key))

    
    return data