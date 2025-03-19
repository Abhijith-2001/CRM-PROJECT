import uuid

from .models import PersonalDetails

import random

import string

# EMAIL REALTED IMPORTS !!!!!

from django.core.mail import EmailMultiAlternatives # we define all parameters in email alternatives
from django.template.loader import render_to_string 
from django.conf import settings


def get_admission_number():
    
    while True:

        pattern = str(uuid.uuid4().int)[:7]
        
        admn_num = f'LM-{pattern}'
        
        if not PersonalDetails.objects.filter(adm_num=admn_num).exists(): # gives a true or false , checks if admn_num not in adm_num
            
            return admn_num
    


def get_password():
    
    password = "".join(random.choices(string.ascii_letters+string.digits,k=8))
    
    return password


# Email Sending

def send_email(subject,recepients,template,context):
    
    sender = settings.EMAIL_HOST_USER
    
    email_obj = EmailMultiAlternatives(subject,from_email=settings.EMAIL_HOST_USER,to=recepients)
                
    content = render_to_string(template,context)
    
    email_obj.attach_alternative(content,'text/html')
    
    email_obj.send()