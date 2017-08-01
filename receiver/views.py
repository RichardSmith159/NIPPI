# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from django.core.cache import cache
from nips.models import Nip
from records.models import NipRecord
from management.models import NIPPILog
from datetime import datetime
import json


# {
#     "nip_pk": "",
#     "data": {
#         "temperature": "",
#     },
#     "time": ""
# }

@csrf_exempt
def receive(request):
    
    if request.method == "POST":
        print request.POST
    
    data_dict = json.loads(request.POST["json_payload"])
    
    print data_dict, type(data_dict)

    if "nip_pk" in data_dict:

        print "A"

        try:
            
            nip = Nip.objects.get(pk = data_dict["nip_pk"])
        
        except Nip.DoesNotExist:

            NIPPILog.objects.create(
                log_type = "E",
                details = "Nip sending bad data: NIP NOT FOUND FROM DATA (pk = %s)" % str(data_dict["nip_pk"])
            )
        
        else:

            if nip.niprecord_set.all().count() >= 1:

                print "B"

                record = nip.niprecord_set.all()[0]
            
            else:

                print "C"
                
                NIPPILog.objects.create(
                    log_type = "A",
                    details = "No nip records found for nip %s. Creating new records." % nip.name
                )

                record = NipRecord.objects.create(
                    nip = nip
                )

                record.setup()
            
            try:
                
                record.log_data(data_dict)
            
            except OSError:

                NIPPILog.objects.create(
                    log_type = "E",
                    details = "Cannot save nip data: LOG ALREADY EXISTS"
                )
            
            else:

                pass


            record.cache_data(data_dict)

    
    else:

        NIPPILog.objects.create(
            log_type = "E",
            details = "Nip sending bad data: NO NIP PK IN DATA"
        )


    return HttpResponse("OK")