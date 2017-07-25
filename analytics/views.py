# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from nips.models import Nip
from . import forms
import form_errors
NIP_ROW_LENGTH = 4

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
            "current_user": "Richard",
            "nip_array": result
        }
    )