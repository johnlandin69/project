from django.urls import path
from BocetoApp import views

urlpatterns = [
   
    path('',views.home, name="index"),
    path('base/',views.base, name="base"),
    # Otras URLs de tu proyecto...
    path('enviar_correo/', views.enviar_correo, name='enviar_correo'),


       
]