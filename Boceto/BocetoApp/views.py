from django.shortcuts import render

# Create your views here.

def home(request):  
   return render(request, "boceto/home.html")

def base(request):  
   return render(request, "boceto/base.html")