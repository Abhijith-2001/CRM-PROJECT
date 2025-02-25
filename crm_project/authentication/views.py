from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm


# Create your views here.

class LoginView(View):
    
    def get(self,request,*args,**kwrags):
        
        form = LoginForm()
        
        data = {'forms':form}
        
        return render(request,'authentication/login.html',context=data)
    
    def post(self,request,*args,**kwargs):
        
        form = LoginForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username,password=password)
            
            if user:
                
                login(request,user)
                
                role = user.role
                
                if role in ['ADMIN','SALES']:
                    
                    return redirect('dashboard')
                
                elif role in ['ACADEMIC COUNSELLOR','TRAINER']:
                    
                    return redirect('students')
                
                elif role in ['STUDENT']:
                    
                    return redirect('recordings')
            
            
                
        error = f'The User {username} Does Not Exists !!'
        
        data = {'forms':form,'error':error}
        
        return render(request,'authentication/login.html',context=data)
    
    
class LogOutView(View):
    
    def get(self,request,*args,**kwrags):
        
        logout(request)
        
        return redirect('login')