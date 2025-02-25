from django.db import models

import uuid

# Create your models here.

class BaseClass(models.Model):
    
    uuid = models.SlugField(unique=True,default=uuid.uuid4)
    
    active_status = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True) # updates with changes
    
    class Meta:         # to make it abstract since it is only inherited.
        
        abstract = True
    
    
    # COURSE CHOICES
    
class CourseChoices(models.TextChoices):
    
    PY_DJANGO = 'PY-DJANGO', 'PY-Django'
    
    MEARN = 'MEARN', 'MEARN'
    
    DATA_SCIENCE = 'DATA-SCIENCE', 'DATA-SCIENCE'
    
    SOFTWARE_TESTING = 'SOFTWARE-TESTING', 'SOFTWARE-TESTING'
    
    
    # DISTRICT CHOICES
    
class DistrictChoices(models.TextChoices):
    
    THIRUVANANTHAPURAM = "Thiruvananthapuram","Thiruvananthapuram"
    
    KOLLAM = "Kollam","Kollam"
    
    PATHANAMTHITTA = "Pathanamthitta","Pathanamthitta"
    
    ALAPPUZHA = "Alappuzha","Alappuzha"
    
    KOTTAYAM = "Kottayam","Kottayam"
    
    IDUKKI = "Idukki","Idukki"
    
    ERNAKULAM = "Ernakulam","Ernakulam"
    
    THRISSUR = "Thrissur","Thrissur"
    
    PALAKKAD = "Palakkad","Palakkad"
    
    MALAPPURAM = "Malappuram","Malappuram"
    
    KOZHIKODE = "Kozhikode","Kozhikode"
    
    WAYANAD = "Wayanad","Wayanad"
    
    KANNUR = "Kannur","Kannur"
    
    KASARAGOD = "Kasaragod","Kasaragod"


class BatchChoices(models.TextChoices):
    
    PY_BATCH_1 = 'PY-NOV-2024','PY-NOV-2024'
    
    PY_BATCH_2 = 'PY-JAN-2025','PY-JAN-2025'
    
    ST_BATCH_1 = 'ST-JAN-2025','ST-JAN-2025'
    
    MEARN_BATCH_1 = 'MEARN-NOV-2024','MEARN-NOV-2024'
    
    MEARN_BATCH_2 = 'MEARN-JAN-2025','MEARN-JAN-2025'
    
    
class TrainerChoices(models.TextChoices):
    
     TRAINER_1 = 'JOHN DOE','JOHN DOE'
     
     TRAINER_2 = 'JAMES','JAMES'
     
     TRAINER_3 = 'PETER','PETER'
     
     TRAINER_4 = 'ALEX','ALEX'
    
    
class PersonalDetails(BaseClass):  
    
    profile         = models.OneToOneField('authentication.Profile',on_delete=models.CASCADE)  
    
    first_name      = models.CharField(max_length=50)
    
    last_name       = models.CharField(max_length=50)
    
    photo           = models.ImageField(upload_to='students')
    
    email           = models.EmailField(unique=True)
    
    contact_num     = models.CharField(max_length=50)
     
    house_name      = models.CharField(max_length=50)
    
    post_office     = models.CharField(max_length=20)
    
    district        = models.CharField(max_length=50,choices=DistrictChoices.choices)
    
    pincode         = models.CharField(max_length=6)
    
    
    # Course Details.
    
    
    adm_num         = models.CharField(max_length=50)
    
    # course          = models.CharField(max_length=50,choices=CourseChoices.choices) # the default parameter is used For providing a default value.
                                                                                # -> default=CourseChoices.PY_DJANGO
    
    # batch           = models.CharField(max_length=50,choices=BatchChoices.choices)
    
    # batch_date      = models.DateField()
    
    course          = models.ForeignKey('courses.Courses',null=True,on_delete=models.SET_NULL)
    
    batch           = models.ForeignKey('batches.Batches',null=True,on_delete=models.SET_NULL)
    
    join_date       = models.DateField(auto_now_add=True)
    
    trainer         = models.ForeignKey('trainers.Trainers',null=True,on_delete=models.SET_NULL)
    
    # trainer_name    = models.CharField(max_length=30,choices=TrainerChoices.choices)
    
    def __str__(self):              # Representaion of Model object
        
        return f'{self.first_name} {self.last_name}'
    
    
    class Meta :                    #Representation of model
        
        verbose_name = 'Personal details'
        
        verbose_name_plural = 'Personal Details'
        
        ordering = ['id']                               # TO define the order the objects are in.-> 'id'-> first created is above,
                                                                                                  # '-id'-> first created is bottom