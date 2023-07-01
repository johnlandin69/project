from django.urls import path
from BocetoApp import views

urlpatterns = [
   
    path('',views.home, name="index"),
       
]