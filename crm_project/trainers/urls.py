from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('trainers/',views.TrainerView.as_view(),name='trainers'),
    path('registertrainer/',views.RegisterView.as_view(),name='registertrainer'),
    path('trainerdetail/<str:uuid>/',views.TrainerDetailView.as_view(),name='trainerdetail'),
    path('trainerdelete/<str:uuid>/',views.TrainerDeleteView.as_view(),name='trainerdelete'),
    path('trainerupdate/<str:uuid>/',views.TrainerUpdateView.as_view(),name='trainerupdate'),
    
    
]
