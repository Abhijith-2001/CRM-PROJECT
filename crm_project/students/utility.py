import uuid

from .models import PersonalDetails

import random

import string


def get_admission_number():
    
    while True:

        pattern = str(uuid.uuid4().int)[:7]
        
        admn_num = f'LM-{pattern}'
        
        if not PersonalDetails.objects.filter(adm_num=admn_num).exists(): # gives a true or false , checks if admn_num not in adm_num
            
            return admn_num
    


def get_password():
    
    password = "".join(random.choices(string.ascii_letters+string.digits,k=8))
    
    return password