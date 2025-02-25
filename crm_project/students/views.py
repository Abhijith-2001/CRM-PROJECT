from django.shortcuts import render,redirect,get_object_or_404

from django.views.generic import View

from .models import DistrictChoices,CourseChoices,BatchChoices,TrainerChoices,PersonalDetails

from .utility import get_admission_number,get_password

from .forms import StudentRegisterForm

from django.db.models import Q

from django.db import transaction  # atomic ->> is used to rollback 

from authentication.models import Profile

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from authentication.permissions import permission_role

# Create your views here.

class GetStudentObject:
    
    def get_student(self,request,uuid):
        
        try:
            
            student = PersonalDetails.objects.get(uuid=uuid)
            
            return student
            
        except:
            
            # return render(request,'students/404.html') OR
            
            return render(request,'errorpages/404.html')
        
        

# @method_decorator(login_required(login_url='login'),name='dispatch')

# @method_decorator(permission_role(roles = ['ADMIN','Sales']),name='dispatch')
class DashBoardView(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'students/dashboard.html')
    
@method_decorator(permission_role(roles = ['ADMIN','Sales','TRAINER','ACADEMIC COUNSELLOR']),name='dispatch')
class StudentView(View):
    
    def get(self,request,*args,**kwargs):
        
        query = request.GET.get('query')
        
        student = PersonalDetails.objects.filter(active_status = True)
        
        if query:
            
            student = PersonalDetails.objects.filter(Q(active_status = True) & (Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__exact=query) | Q(contact_num__icontains=query) | Q(house_name__icontains=query) | Q(post_office__icontains=query) | Q(pincode__icontains=query)   | Q(district__icontains=query) | Q(batch__name__icontains=query) | Q(course__code__icontains=query) | Q(trainer__first_name__icontains=query) | Q(adm_num__icontains=query)))
                                                                                                                # __contains is used to check if it is there in the var.case sensitive.only works with text or char field.
                                                                                                                # __icontains is used to check if it is there in the var.case insensitive.only works with text or char field.
                                                                                                                # __name is used in case of foreign key fields like course,batch,...etc.
        
        # student = PersonalDetails.objects.all()
        
        
        data = {'students':student,'query':query}
        
        return render(request,'students/students.html',context=data)
    
    
    
@method_decorator(permission_role(roles = ['ADMIN','Sales']),name='dispatch')
class RegisterView(View):
    
    def get(self,request,*args,**kwargs):
        
        forms = StudentRegisterForm()
        
        # data = {'districts':DistrictChoices,'courses':CourseChoices,'batches':BatchChoices,'trainers':TrainerChoices,'forms':forms}
        
        data = {'forms':forms}
        
        return render(request,'students/registeration.html',context=data)
    
    def post(self,request,*args,**kwargs):
        
        form = StudentRegisterForm(request.POST,request.FILES)
        
        if form.is_valid():
            
            with transaction.atomic():
            
                student = form.save(commit=False)
                
                student.adm_num = get_admission_number()
                
                username = student.email
                
                password = get_password()
                
                print(password)  # Note Password from Terminal. 
                                    # >>  Renji@gmail.com - CDwfmw3T 
                                    # >> vishnu@gmail.com - cLazxyzQ
                
                profile  =  Profile.objects.create_user(username=username,password=password,role='STUDENT')
                
                student.profile = profile
                
                student.save()
            
            return redirect('students')
        
        else:
            
            data = {'forms':form}
        
            return render(request,'students/registeration.html',context=data)
        
    #     form_data      = request.POST
        
    #     first_name      =   form_data.get('first_name')
        
    #     last_name       =   form_data.get('last_name')
        
    #     photo           =   request.FILES.get('photo') # to obtain the Image or files from THE FORM.
        
    #     email           =   form_data.get('email')
        
    #     contact_num     =   form_data.get('contact')
        
    #     house_name      =   form_data.get('house_name')
        
    #     post_office     =   form_data.get('post_office')
        
    #     district        =   form_data.get('district')
        
    #     pincode         =   form_data.get('pincode')
        
    #     adm_num         =   get_admission_number()
        
    #     course          =   form_data.get('course')
        
    #     batch           =   form_data.get('batch')
        
    #     batch_date      =   form_data.get('batch_date')
        
    #     join_date       =   '2025-01-31'
        
    #     trainer_name    =   form_data.get('trainer')
        
    #     print(first_name,last_name,photo,email,contact_num,house_name,post_office,district,pincode,adm_num,course,batch,batch_date,join_date,trainer_name)
        
    #     PersonalDetails.objects.create(first_name = first_name,
    #                                     last_name = last_name,
    #                                     photo = photo,
    #                                     email = email,
    #                                     contact_num = contact_num,
    #                                     house_name = house_name,
    #                                     post_office = post_office,
    #                                     district = district,
    #                                     pincode = pincode,
    #                                     adm_num = adm_num,
    #                                     course = course,
    #                                     batch = batch,
    #                                     batch_date = batch_date,
    #                                     join_date = join_date,
    #                                     trainer_name = trainer_name)
        


class StudentDetailView(View):
    
    def get(self,request,*args,**kwargs):
        
        uuid = kwargs.get('uuid')
        
        # students = get_object_or_404(PersonalDetails,uuid=uuid)  # Used For default 404 page,and to use this without try and except.
        
        student = GetStudentObject().get_student(request,uuid)
        
        data = {'student':student}
        
        return render(request,'students/student-detail.html',context=data)
    
# class Error404View(View):
    
#     def get(self,request,*args,**kwargs):
        
#         return render(request,'students/404.html')
    
# class Error403View(View):
    
#     def get(self,request,*args,**kwargs):
        
#         return render(request,'errorpages/error-403.html')

    
    
# @method_decorator(permission_role(roles = ['ADMIN','Sales']),name='dispatch') 
class StudentDeleteView(View):
    
    
    def get(self,request,*args,**kwargs):
        
        uuid = kwargs.get('uuid')
        
        # students = get_object_or_404(PersonalDetails,uuid=uuid)  # Used For default 404 page,and to use this without try and except.
        
        student = GetStudentObject().get_student(request,uuid)
        
        data = {'student':student}
        
        # student.delete()
        student.active_status = False
        
        student.save()
        
        return redirect('students')
    
    
@method_decorator(permission_role(roles = ['ADMIN','Sales']),name='dispatch')
class StudentUpdateView(View):
    
    def get(self,request,*args,**kwargs):
        
        uuid = kwargs.get('uuid')
        
        student = GetStudentObject().get_student(request,uuid)
        
        form = StudentRegisterForm(instance=student)    # to display the data of the id called use parameter -> instance
        
        data = {'forms':form}
        
        return render (request,'students/student-update.html',context=data)
    
    
    
    def post(self,request,*args,**kwargs):
        
        uuid = kwargs.get('uuid')
        
        student = GetStudentObject().get_student(request,uuid)
        
        form = StudentRegisterForm(request.POST,request.FILES,instance=student)    # to display the data of the id called use parameter -> instance
        
        
        if form.is_valid():
            
            form.save()
            
            return redirect('students')
        
        else:

            data = {'forms':form}
        
            return render (request,'students/student-update.html',context=data)