# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from nips.models import Nip

NIP_ROW_LENGTH = 4

def overview(request):

    nips = Nip.objects.all()

    result = [nips[i:i+NIP_ROW_LENGTH] for i in xrange(0, len(nips), NIP_ROW_LENGTH)]

    if len(result[-1]) < NIP_ROW_LENGTH:
        while len(result[-1]) < NIP_ROW_LENGTH:
            result[-1].append("EMPTY")
    
    result.append(["EMPTY"]*4)

    print result
    return render(
        request,
        "analytics/analyticsDashboard.html",
        {
            "current_user": "Richard",
            "nip_array": result
        }
    )