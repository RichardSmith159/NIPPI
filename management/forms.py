from django import forms
from django.db import IntegrityError
from nips.models import NipLocation, Nip
from django.contrib import messages
from django.contrib.auth.models import User

import passwordGen

class AddNipForm(forms.Form):

    new_nip_name = forms.CharField(max_length = 20, required = True)
    new_nip_location_pk = forms.IntegerField(required = True)

    def process(self, request):

        cleaned_new_nip_name = self.cleaned_data["new_nip_name"]
        cleaned_new_nip_location_pk = self.cleaned_data["new_nip_location_pk"]

        try:

            selected_location = NipLocation.objects.get(pk = cleaned_new_nip_location_pk)

        except NipLocation.DoesNotExist:

            messages.error(request, "The selected location could not be found in the database.")
        
        else:


            try:

                nip = Nip.objects.get(name = cleaned_new_nip_name)
            
            except Nip.DoesNotExist:

                new_nip = Nip.objects.create(
                    name = cleaned_new_nip_name,
                    location = selected_location
                )

                new_nip.generate_uid()

                messages.success(request, "The new nip '%s' was created successfully." % cleaned_new_nip_name)

            else:

                messages.error(request, "A nip with name '%s' already exists. Nip names must be unique." % cleaned_new_nip_name)

        

class DeleteUserForm(forms.Form):

    user_pk = forms.IntegerField(required = True)

    def process(self, request):

        cleaned_user_pk = self.cleaned_data["user_pk"]

        try:

            selected_user = User.objects.get(pk = cleaned_user_pk)
            username = selected_user.username

        except User.DoesNotExist:

            messages.error(request, "The selected user could not be found in the database.")
        
        else:

            selected_user.delete()

            messages.success(request, "The selected user '%s' was deleted successfully." % username)


class AddUserForm(forms.Form):

    new_username = forms.CharField(max_length = 50, required = True)
    new_email = forms.EmailField(required = True)

    def process(self, request):

        cleaned_new_username = self.cleaned_data["new_username"]
        cleaned_new_email = self.cleaned_data["new_email"]

        try:

            existing_user = User.objects.get(username = cleaned_new_username)
        
        except User.DoesNotExist:

            try:

                existing_user = User.objects.get(email = cleaned_new_email)
            
            except User.DoesNotExist:

                new_password = passwordGen.generate_code(10)

                new_user = User.objects.create_user(
                    username = cleaned_new_username,
                    password = new_password,
                    email = cleaned_new_email
                )

                messages.success(request, "The user account was created successfully.")
            
            else:

                messages.error(request, "A user with the email '%s' already exists." % cleaned_new_email)
        
        else:

            messages.error(request, "A user with the username '%s' already exists." % cleaned_new_username)



class DeleteLocationForm(forms.Form):

    location_pk_for_deletion = forms.IntegerField(required = True)

    def process(self, request):

        cleaned_pk = self.cleaned_data["location_pk_for_deletion"]

        try:

            selected_location = NipLocation.objects.get(pk = cleaned_pk)
        
        except NipLocation.DoesNotExist:

            messages.error(request, "Could not find the Location in database.")
        
        else:

            selected_location.delete()

            messages.success(request, "The location was deleted successfully.")
            

class AddLocationForm(forms.Form):

    new_location_name = forms.CharField(max_length = 30, required = True)

    def process(self, request):

        cleaned_new_location_name = self.cleaned_data["new_location_name"]

        try:

            existing_location = NipLocation.objects.get(name = cleaned_new_location_name)
        
        except NipLocation.DoesNotExist:

            new_location = NipLocation.objects.create(name = cleaned_new_location_name)
            messages.success(request, "The location '%s' was created successfully." % cleaned_new_location_name)
        
        else:

            messages.error(
                request,
                "A location with the name '%s' already exists. Location names must be unique." % cleaned_new_location_name
            )