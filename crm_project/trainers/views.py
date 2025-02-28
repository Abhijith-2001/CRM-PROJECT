from django.shortcuts import render,redirect,get_object_or_404

from django.views.generic import View

from .models import Trainers

from .utility import get_password,get_trainer_id

from .forms import TrainerRegisterForm

from django.db.models import Q

from django.db import transaction  # atomic ->> is used to rollback 

from authentication.models import Profile

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from authentication.permissions import permission_role

# Create your views here.

class GetTrainerObject:
    
    def get_trainer(self,request,uuid):
        
        try:
            
            trainer = Trainers.objects.get(uuid=uuid)
            
            return trainer
            
        except:
            
            # return render(request,'students/404.html') OR
            
            return render(request,'errorpages/404.html')
        
    
# @method_decorator(permission_role(roles = ['ADMIN','Sales','TRAINER','ACADEMIC COUNSELLOR']),name='dispatch')
class TrainerView(View):
    
    def get(self,request,*args,**kwargs):
        
        trainer = Trainers.objects.all()

        data = {'trainers':trainer}
        
        return render(request,'trainers/trainers.html',context=data)
    
    # def get(self, request, *args, **kwargs):
    #     query = request.GET.get('query')
        
    #     # Base Queryset
    #     trainer = Trainers.objects.filter(active_status=True)
            
    #     if query:
    #         search_filters = Q(first_name__icontains=query) | Q(last_name__icontains=query) | \
    #                         Q(email__exact=query) | Q(contact__icontains=query) | \
    #                         Q(house_name__icontains=query) | Q(post_office__icontains=query) | \
    #                         Q(pincode__icontains=query) | Q(district__icontains=query) | \
    #                         Q(qualification__icontains=query) | Q(course__code__icontains=query) | \
    #                         Q(stream__icontains=query) | Q(employee_id__icontains=query)

    #         trainer = trainer.filter(search_filters)

    #     return render(request, 'students/students.html', {'students': trainer, 'query': query})
        
    
    
@method_decorator(permission_role(roles = ['ADMIN','Sales']),name='dispatch')
class RegisterView(View):
    
    def get(self,request,*args,**kwargs):
        
        trainer_forms = TrainerRegisterForm()
        
        data = {'forms':trainer_forms}
        
        return render(request,'trainers/registration.html',context=data)
    
    def post(self,request,*args,**kwargs):
        
        form = TrainerRegisterForm(request.POST,request.FILES)
        
        if form.is_valid():
            
            with transaction.atomic():
            
                trainer = form.save(commit=False)
                
                trainer.employee_id = get_trainer_id()
                
                username = trainer.email
                
                password = 'trainer123'
                
                profile  =  Profile.objects.create_user(username=username,password=password,role='TRAINER')
                
                trainer.profile = profile
                
                trainer.save()
            
            return redirect('trainers')
        
        else:
            
            data = {'forms':form}
        
            return render(request,'trainers/registration.html',context=data)
        


class TrainerDetailView(View):
    
    def get(self,request,*args,**kwargs):
        
        uuid = kwargs.get('uuid')
        
        # students = get_object_or_404(PersonalDetails,uuid=uuid)  # Used For default 404 page,and to use this without try and except.
        
        trainer = GetTrainerObject().get_trainer(request,uuid)
        
        data = {'trainer':trainer}
        
        return render(request,'trainers/trainer-detail.html',context=data)
    




@method_decorator(permission_role(roles = ['ADMIN','Sales']),name='dispatch') 
class TrainerDeleteView(View):
    
    
    def get(self,request,*args,**kwargs):
        
        uuid = kwargs.get('uuid')
        
        # trainers = get_object_or_404(PersonalDetails,uuid=uuid)  # Used For default 404 page,and to use this without try and except.
        
        trainer = GetTrainerObject().get_trainer(request,uuid)
        
        # data = {'trainer':trainer}
        
        # trainer.delete()
        trainer.active_status = False
        
        trainer.save()
        
        return redirect('trainers')
    
    
@method_decorator(permission_role(roles = ['ADMIN','Sales']),name='dispatch')
class TrainerUpdateView(View):
    
    def get(self,request,*args,**kwargs):
        
        uuid = kwargs.get('uuid')
        
        trainer = GetTrainerObject().get_trainer(request,uuid)
        
        form = TrainerRegisterForm(instance=trainer)    # to display the data of the id called use parameter -> instance
        
        data = {'forms':form}
        
        return render (request,'trainers/trainer-update.html',context=data)
    
    
    
    def post(self,request,*args,**kwargs):
        
        uuid = kwargs.get('uuid')
        
        trainer = GetTrainerObject().get_trainer(request,uuid)
        
        form = TrainerRegisterForm(request.POST,request.FILES,instance=trainer)    # to display the data of the id called use parameter -> instance
        
        
        if form.is_valid():
            
            form.save()
            
            return redirect('trainers')
        
        else:

            data = {'forms':form}
        
            return render (request,'trainers/trainer-update.html',context=data)