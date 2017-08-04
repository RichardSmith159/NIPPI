# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from nips.models import Nip
from . import forms
import form_errors
from siren.models import Siren, Alert
from django.contrib.auth import logout
import json
import pprint
NIP_ROW_LENGTH = 4



def get_siren_data(request, siren_pk):

    data = {}

    try:

        selected_siren = Siren.objects.get(pk = siren_pk)
    
    except Siren.DoesNotExist:

        data = {"status": "ERROR", "message": "SIREN_NOT_FOUND"}
    
    else:
        
        data = {
            "name": selected_siren.name,
            "registered_users": [user.username for user in selected_siren.registered_users.all()],
            "monitor_variable": selected_siren.monitor_variable,
            "tolerance": selected_siren.tolerance,
            "acceptable_bounds_upper_limit": selected_siren.acceptable_bounds_upper_limit,
            "acceptable_bounds_lower_limit": selected_siren.acceptable_bounds_lower_limit,
            "message": selected_siren.message,
            "email_notification": selected_siren.email_notification,
            "text_notification": selected_siren.text_notification
        }
        
        if selected_siren.creator:

            data["creator"] = selected_siren.creator.username
        
        else:

            data["creator"] = "UNKNOWN"
        
        

            

    return HttpResponse(json.dumps(data), content_type='application/json')



def get_historical_data(request, nip_pk, timescale):

    allowed_timescales = [
        "TODAY",
        "24HOURS",
        "WEEK",
        "HOUR",
        "15MINS",
        "ALL"
    ]

    try:

        selected_nip = Nip.objects.get(pk = nip_pk)
    
    except Nip.DoesNotExist:

        data = {"status": "ERROR", "message": "NIP_NOT_FOUND"}
    
    else:

        try:

            selected_record = selected_nip.niprecord_set.all()[0]
        
        except NipRecord.DoesNotExist:

            data = {"STATUS": "ERROR", "message": "RECORDS_NOT_FOUND"}
        
        else:

            if timescale not in allowed_timescales:

                data = {"status": "ERROR", "message": "TIMESCALE_NOT_ALLOWED"}
            
            elif timescale == "TODAY":

                data = selected_record.get_todays_data()
            
            elif timescale == "24HOURS":

                data = selected_record.get_past_24_hours()
            
            elif timescale == "WEEK":

                data = selected_record.get_past_week()
            
            elif timescale == "HOUR":

                data = selected_record.get_past_hour()
            
            elif timescale == "15MINS":

                data = selected_record.get_past_quarter_hour()
            
            elif timescale == "ALL":

                data = selected_record.get_all_data()
            
            else:

                data = {"status": "WARNING", "message": "TIMESCALE_NOT_IMPLEMENTED"}
    
    for point in data["data"]:
        print point

    return HttpResponse(json.dumps(data), content_type='application/json')




def logout_user(request):

    logout(request)

    return redirect("analytics:login")



def login_user(request):

    if request.method == "POST":

        login_form = forms.LoginForm(request.POST)

        if login_form.is_valid():

            success = login_form.process(request)

            if success:

                return redirect("analytics:overview")
            
            else:

                messages.error(request, "Username or password was incorrect.")
        
        else:

            form_errors.convert_form_errors_to_messages(login_form, request)
    
    else:

        login_form = forms.LoginForm()

    return render(
        request,
        "analytics/login.html",
        {
            "login_form": login_form
        }
    )



def overview(request):

    nips = Nip.objects.all()

    result = [nips[i:i+NIP_ROW_LENGTH] for i in xrange(0, len(nips), NIP_ROW_LENGTH)]

    if len(result[-1]) < NIP_ROW_LENGTH:
        while len(result[-1]) < NIP_ROW_LENGTH:
            result[-1].append("EMPTY")

    return render(
        request,
        "analytics/analyticsDashboard.html",
        {
            "current_user": request.user.username,
            "nip_array": result
        }
    )



def nip_details(request, nip_pk):

    respond_to_alert_form = forms.RespondToAlertForm()
    add_siren_form = forms.AddSirenForm()

    if request.method == "POST":

        if "add_siren_form" in request.POST:

            add_siren_form = forms.AddSirenForm(request.POST)

            if add_siren_form.is_valid():

                add_siren_form.process(request)
            
            else:

                form_errors.convert_form_errors_to_messages(add_siren_form, request)

            

        if "respond_to_alert_form" in request.POST:
                
            respond_to_alert_form = forms.RespondToAlertForm(request.POST)

            if respond_to_alert_form.is_valid():

                respond_to_alert_form.process(request)
            
            else:

                form_errors.convert_form_errors_to_messages(respond_to_alert_form, request)


    try:

        nip = Nip.objects.get(pk = nip_pk)
    
    except Nip.DoesNotExist:

        pass
        # redirect to 404 page
    
    else:

        pass
        
        alerts = Alert.objects.filter(siren__nip = nip).order_by("status")

    return render(
        request,
        "analytics/details.html",
        {
            "nip": nip,
            "alerts": alerts,
            "add_siren_form": add_siren_form,
            "respond_to_alert_form": respond_to_alert_form
        }
    )