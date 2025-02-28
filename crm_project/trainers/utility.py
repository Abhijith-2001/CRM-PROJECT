import uuid

from .models import Trainers

import random

import string


def get_trainer_id():
    
    while True:

        pattern = str(uuid.uuid4().int)[:5]
        
        employee_id = f'LM-E{pattern}'
        
        if not Trainers.objects.filter(employee_id=employee_id).exists(): # gives a true or false , checks if employee_id not in adm_num
            
            return employee_id
    


def get_password():
    
    password = "".join(random.choices(string.ascii_letters+string.digits,k=8))
    
    return password