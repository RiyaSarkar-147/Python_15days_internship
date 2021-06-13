from django.http.response import HttpResponse
from django.shortcuts import render 
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def register(request):
    return render(request,'register.html')
    
def about(request):
    return render(request,'about.html')
    
