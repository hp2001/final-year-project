from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    # form = UserCreationForm
    return render(request, 'login.html')

def register(request):
    
    return render(request, 'register.html')