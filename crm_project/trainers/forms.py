# from batches.models import Batches

from django import forms
from .models import Trainers,DistrictChoices,BaseClass
from courses.models import Courses

class TrainerRegisterForm(forms.ModelForm):
    
    class Meta :
        
        model = Trainers
        
        # fields = ['first_name','last_name','photo','email','contact_num','house_name','post_office','district',
        #           'pincode','course','batch','batch_date','trainer_name']
        
        
        # fields = '__all__' # when all the fields are used or inputted by user use magic method __all__
        
        
        exclude =   ['employee_id','uuid','active_status','profile'] # the fields that are not required.
        
        # widgets attribute is used to bring style to the HTML page.
        
        # attrs defined as dictionary 
        # things like class,place holder,required etc.
        
        widgets = {'first_name':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                       'required':'required'}),
                   'last_name':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                       'required':'required'}),
                   'photo':forms.FileInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
                                                       }),
                   'id_card':forms.FileInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
                                                       }),
                   'email':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                       'required':'required'}),
                   'contact':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                       'required':'required'}),
                   'house_name':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                       'required':'required'}),
                   'post_office':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                       'required':'required'}),
                   'qualification':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                       'required':'required'}),
                   'stream':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                       'required':'required'}),
                   'pincode':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                       'required':'required'}),}
                #    'batch_date':forms.DateInput(attrs={'type':'date','class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                #                                        'required':'required'}),}
        
    district = forms.ChoiceField(
        choices=DistrictChoices.choices,  # Ensure DistrictChoices is correctly defined
        widget=forms.Select(
            attrs={
                "class": "block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 "
                         "focus:border-purple-400 focus:outline-none focus:shadow-outline-purple "
                         "dark:focus:shadow-outline-gray form-select"
            }
        )
    )
    
    course = forms.ModelChoiceField(queryset=Courses.objects.all(),widget=forms.Select(
            attrs={"class": "block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 "
                         "focus:border-purple-400 focus:outline-none focus:shadow-outline-purple "
                         "dark:focus:shadow-outline-gray form-select"
                         }))


    def clean(self):
        
        cleaned_data = super().clean()
        
        pincode = cleaned_data.get('pincode')
        
        email = cleaned_data.get('email')
        
        # Check if the instance exists (i.e., it's not a new object)
        
        if not self.instance.uuid:  # this means the object doesn't exist yet (new registration)
            
            if Trainers.objects.filter(profile__username=email).exists():
                self.add_error('email', "This Email is already Registered")
        
        if len(str(pincode)) < 6:
            self.add_error('pincode', 'Pincode must be 6 digits!')
            
        return cleaned_data

    
    
    def __init__(self, *args, **kwargs):
        
        super(TrainerRegisterForm,self).__init__(*args,**kwargs)
        
        if not self.instance:
        
            self.fields.get('photo').widget.attrs['required'] = 'required'
            self.fields.get('id_card').widget.attrs['required'] = 'required'


