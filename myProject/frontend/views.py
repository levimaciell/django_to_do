from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def login(request):
    pass

def register(request):
    return HttpResponse('This should be a Register page')

def todo(request):

    response = requests.get('http://127.0.0.1:8080/api/todo')

    if response.status_code == 200:
        tasks = response.json()
    else:
        tasks = 'Loading...'
    
    context = {'tasks': tasks}
    return render(request, 'frontend/index.html', context)