from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('dashboard/',views.DashBoardView.as_view(),name='dashboard'),
    path('students/',views.StudentView.as_view(),name='students'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('student-detail/<str:uuid>/',views.StudentDetailView.as_view(),name='student-detail'),
    # path('error-404/',views.Error404View.as_view(),name='error-404'),
    # path('error-403/',views.Error403View.as_view(),name='error-403'),
    path('studentdelete/<str:uuid>/',views.StudentDeleteView.as_view(),name='studentdelete'),
    path('studentupdate/<str:uuid>/',views.StudentUpdateView.as_view(),name='studentupdate'),
    
    
]
