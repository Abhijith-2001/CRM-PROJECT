from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('recordings/',views.RecordingsView.as_view(),name='recordings'),
]