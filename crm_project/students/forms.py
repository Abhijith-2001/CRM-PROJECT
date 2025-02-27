from django import forms
from .models import PersonalDetails,DistrictChoices,BatchChoices,TrainerChoices,CourseChoices,BaseClass

from batches.models import Batches
from courses.models import Courses
from trainers.models import Trainers

class StudentRegisterForm(forms.ModelForm):
    
    class Meta :
        
        model = PersonalDetails
        
        # fields = ['first_name','last_name','photo','email','contact_num','house_name','post_office','district',
        #           'pincode','course','batch','batch_date','trainer_name']
        
        
        # fields = '__all__' # when all the fields are used or inputted by user use magic method __all__
        
        
        exclude =   ['adm_num','join_date','uuid','active_status','profile'] # the fields that are not required.
        
        # widgets attribute is used to bring style to the HTML page.
        
        # attrs defined as dictionary 
        # things like class,place holder,required etc.
        
        widgets = {'first_name':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                       'required':'required'}),
                   'last_name':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                       'required':'required'}),
                   'photo':forms.FileInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
                                                       }),
                   'email':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                       'required':'required'}),
                   'contact_num':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                       'required':'required'}),
                   'house_name':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                       'required':'required'}),
                   'post_office':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
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
    
    batch = forms.ModelChoiceField(queryset=Batches.objects.all(),widget=forms.Select(
            attrs={"class": "block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 "
                         "focus:border-purple-400 focus:outline-none focus:shadow-outline-purple "
                         "dark:focus:shadow-outline-gray form-select"
                         }))
    
    course = forms.ModelChoiceField(queryset=Courses.objects.all(),widget=forms.Select(
            attrs={"class": "block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 "
                         "focus:border-purple-400 focus:outline-none focus:shadow-outline-purple "
                         "dark:focus:shadow-outline-gray form-select"
                         }))
    
    trainer = forms.ModelChoiceField(queryset=Trainers.objects.all(),widget=forms.Select(
            attrs={"class": "block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 "
                         "focus:border-purple-400 focus:outline-none focus:shadow-outline-purple "
                         "dark:focus:shadow-outline-gray form-select"
                         }))
    
    # course = forms.ChoiceField(
    #     choices=CourseChoices.choices,
    #     widget=forms.Select(
    #         attrs={
    #             "class": "block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 "
    #                      "focus:border-purple-400 focus:outline-none focus:shadow-outline-purple "
    #                      "dark:focus:shadow-outline-gray form-select"
    #         }
    #     )
    # )
    
    # batch = forms.ChoiceField(
    #     choices=BatchChoices.choices,  # Ensure DistrictChoices is correctly defined
    #     widget=forms.Select(
    #         attrs={
    #             "class": "block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 "
    #                      "focus:border-purple-400 focus:outline-none focus:shadow-outline-purple "
    #                      "dark:focus:shadow-outline-gray form-select"
    #         }
    #     )
    # )
    
    # trainer_name = forms.ChoiceField(
    #     choices=TrainerChoices.choices,  # Ensure DistrictChoices is correctly defined
    #     widget=forms.Select(
    #         attrs={
    #             "class": "block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 "
    #                      "focus:border-purple-400 focus:outline-none focus:shadow-outline-purple "
    #                      "dark:focus:shadow-outline-gray form-select"
    #         }
    #     )
    # )
    
    
    # def clean(self):
        
    #     cleaned_data = super().clean()
        
    #     pincode = cleaned_data.get('pincode')
        
    #     email = cleaned_data.get('email')
        
    #     if PersonalDetails.objects.filter(profile__username = email).exists():
            
    #         self.add_error('email',"This Email is already Registered")
        
    #     if len(str(pincode))<6:
            
    #         self.add_error('pincode','pincode Must Be 6 Digits !!!!!')
            
    #     return cleaned_data
    
    
    def clean(self):
        
        cleaned_data = super().clean()
        
        pincode = cleaned_data.get('pincode')
        
        email = cleaned_data.get('email')
        
        # Check if the instance exists (i.e., it's not a new object)
        
        if not self.instance.uuid:  # this means the object doesn't exist yet (new registration)
            
            if PersonalDetails.objects.filter(profile__username=email).exists():
                self.add_error('email', "This Email is already Registered")
        
        if len(str(pincode)) < 6:
            self.add_error('pincode', 'Pincode must be 6 digits!')
            
        return cleaned_data

    
    
    def __init__(self, *args, **kwargs):
        
        super(StudentRegisterForm,self).__init__(*args,**kwargs)
        
        if not self.instance:
        
            self.fields.get('photo').widget.attrs['required'] = 'required'