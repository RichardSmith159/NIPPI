from django import forms
from django.contrib.auth import authenticate, login
from django.contrib import messages
from siren.models import Alert


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