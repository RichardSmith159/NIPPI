from django.contrib import messages
import json


def convert_form_errors_to_messages(form, request):

    error_dict = json.loads(form.errors.as_json())
    
    for key in error_dict:
        for error in error_dict[key]:
            messages.error(request, "Error: %s - %s" % (key, error["message"]))