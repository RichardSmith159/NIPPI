from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):

    username = forms.CharField(max_length = 40, required = True)
    password = forms.CharField(max_length = 40, required = True)

    def process(self, request):

        cleaned_username = self.cleaned_data["username"]
        cleaned_password = self.cleaned_data["password"]

        return authenticate(username = cleaned_username, password = cleaned_password)