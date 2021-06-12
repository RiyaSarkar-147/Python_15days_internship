from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return HttpResponse("Welcome to Django")

def aboutpageview(request):
    return HttpResponse("About us Page")

def contactpageview(request):
    return HttpResponse("Contact us Page")
