from django import forms
from django.contrib.auth import authenticate, login
from django.contrib import messages
from siren.models import Alert, Siren
from nips.models import Nip

class AddSirenForm(forms.Form):

    nip_pk = forms.IntegerField(required = True)
    name = forms.CharField(required = True, max_length = 30)
    monitor_variable = forms.CharField(required = True, max_length = 30)
    tolerance = forms.IntegerField(required = True)
    acceptable_bounds_upper_limit = forms.FloatField(required = True)
    acceptable_bounds_lower_limit = forms.FloatField(required = True)
    new_siren_message = forms.CharField(required = True, max_length = 100)
    email_notification = forms.BooleanField(required = False)
    text_notification = forms.BooleanField(required = False)

    def process(self, request):

        cleaned_nip_pk = self.cleaned_data["nip_pk"]
        cleaned_name = self.cleaned_data["name"]
        cleaned_monitor_variable = self.cleaned_data["monitor_variable"]
        cleaned_tolerance = self.cleaned_data["tolerance"]
        cleaned_acceptable_bounds_upper_limit = self.cleaned_data["acceptable_bounds_upper_limit"]
        cleaned_acceptable_bounds_lower_limit = self.cleaned_data["acceptable_bounds_lower_limit"]
        cleaned_message = self.cleaned_data["new_siren_message"]
        cleaned_email_notification = self.cleaned_data["email_notification"]
        cleaned_text_notification = self.cleaned_data["text_notification"]

        Siren.objects.create(
            name = cleaned_name,
            nip = Nip.objects.get(pk = cleaned_nip_pk),
            monitor_variable = cleaned_monitor_variable,
            tolerance = cleaned_tolerance,
            acceptable_bounds_upper_limit = cleaned_acceptable_bounds_upper_limit,
            acceptable_bounds_lower_limit = cleaned_acceptable_bounds_lower_limit,
            message = cleaned_message,
            email_notification = cleaned_email_notification,
            text_notification = cleaned_text_notification
        )

        messages.success(request, "The new siren '%s' was created successfully." % cleaned_name)




class RespondToAlertForm(forms.Form):

    seen = forms.BooleanField(required = False)
    handled = forms.BooleanField(required = False)
    alert_pk = forms.IntegerField(required = True)

    def process(self, request):

        cleaned_seen = self.cleaned_data["seen"]
        cleaned_handled = self.cleaned_data["handled"]
        cleaned_alert_pk = self.cleaned_data["alert_pk"]

        try:

            alert = Alert.objects.get(pk = cleaned_alert_pk)

        except Alert.DoesNotExist:

            messages.error(request, "The alert could not be found in the database.")
        
        else:

            if cleaned_seen:

                alert.status = "S"
                alert.seen_by.add(request.user.id)
                alert.save()

                messages.info(
                    request,
                    "Alert status changed to 'seen' and you have been added to the list of responders."
                )

            if cleaned_handled:

                alert.status = "H"
                if request.user not in alert.seen_by.all():
                    alert.seen_by.add(request.user.id)
                
                alert.handled_by = request.user
                alert.save()

                messages.success(request, "Alert status changed to 'handled'. Problem solved.")
            


class LoginForm(forms.Form):

    username = forms.CharField(max_length = 40, required = True)
    password = forms.CharField(max_length = 40, required = True)

    def process(self, request):

        cleaned_username = self.cleaned_data["username"]
        cleaned_password = self.cleaned_data["password"]

        user = authenticate(username = cleaned_username, password = cleaned_password)
        
        if user:

            login(request, user)

            return True

        else:

            return False