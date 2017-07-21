# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from . import forms
import form_errors
from nips.models import Nip, NipLocation




def management_dashboard(request):

    add_location_form = forms.AddLocationForm()
    delete_location_form = forms.DeleteLocationForm()

    add_user_form = forms.AddUserForm()
    delete_user_form = forms.DeleteUserForm()

    add_nip_form = forms.AddNipForm()
    

    if request.method == "POST":

        if "add_nip_form" in request.POST:

            add_nip_form = forms.AddNipForm(request.POST)

            if add_nip_form.is_valid():

                add_nip_form.process(request)
            
            else:

                form_errors.convert_form_errors_to_messages(add_nip_form, request)


        if "delete_user_form" in request.POST:

            delete_user_form = forms.DeleteUserForm(request.POST)

            if delete_user_form.is_valid():

                delete_user_form.process(request)
            
            else:

                form_errors.convert_form_errors_to_messages(delete_user_form, request)

        if "add_user_form" in request.POST:

            add_user_form = forms.AddUserForm(request.POST)

            if add_user_form.is_valid():

                add_user_form.process(request)

            else:

                form_errors.convert_form_errors_to_messages(add_user_form, request)


        if "delete_location_form" in request.POST:

            delete_location_form = forms.DeleteLocationForm(request.POST)

            if delete_location_form.is_valid():

                delete_location_form.process(request)
            
            else:

                form_errors.convert_form_errors_to_messages(delete_location_form, request)


        if "add_location_form" in request.POST:

            add_location_form = forms.AddLocationForm(request.POST)

            if add_location_form.is_valid():

                add_location_form.process(request)
            
            else:

                form_errors.convert_form_errors_to_messages(add_location_form, request)


    return render(
        request,
        "management/managementDashboard.html",
        {
            "users": User.objects.all(),
            "locations": NipLocation.objects.all(),
            "nips": Nip.objects.all(),
            "current_user": "Richard",
            "add_location_form": add_location_form,
            "delete_location_form": delete_location_form,
            "add_user_form": add_user_form,
            "delete_user_form": delete_user_form,
            "add_nip_form": add_nip_form
        }
    )


def nip_management(request):

    return render(request, "", {})