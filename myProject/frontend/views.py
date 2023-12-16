from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return HttpResponse('This should be a login page')

def register(request):
    return HttpResponse('This should be a Register page')

def todo(request):
    return HttpResponse('This should be where todos are listed')