from django.db import models

# Create your models here.

from students.models import BaseClass

class PaymentSettleChoices(models.TextChoices):
    
    ONE_TIME = 'One Time','One Time'
    
    INSTALLMENTS = 'Installments','Installments'
    
class InstallmentChoices(models.IntegerChoices):
    
    TWO   = 2,'2'
    THREE = 3,'3'
    FOUR  = 4,'4'
    FIVE  = 5,'5'
    SIX   = 6,'6'

class PaymentStructure(BaseClass):
    
    student = models.OneToOneField('students.PersonalDetails',on_delete=models.CASCADE)
    
    one_time_or_installments  = models.CharField(max_length=25,choices=PaymentSettleChoices.choices)
    
    no_of_installments = models.IntegerField(choices=InstallmentChoices.choices,null=True,blank=True)
    
    fee_to_be_paid = models.FloatField()
    
    
    
    
    def __str__(self):              # Representaion of Model object
        
        return f'{self.student.first_name} {self.student.batch.name}'
    
    
    class Meta :                    #Representation of model
        
        verbose_name = 'Payment Structure'
        
        verbose_name_plural = 'Payment Structure'
        
        ordering = ['id']                               # TO define the order the objects are in.-> 'id'-> first created is above,
                                                                                                  # '-id'-> first created is bottom