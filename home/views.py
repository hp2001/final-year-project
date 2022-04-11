from tkinter.messagebox import RETRY
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def home(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

"""
def login(request):
    form = UserCreationForm
    return render(request, 'login.html',{'form':form})

def register(request):
    return render(request, 'register.html')
"""

def tcs(request):
    context = {
        'companyName': "TCS"
    }
    return render(request, 'stockDetail.html', context)


def fis(request):
    context = {
        'companyName': "FIS"
    }
    return render(request, 'stockDetail.html', context)


def epam(request):
    context = {
        'companyName': "EPAM"
    }
    return render(request, 'stockDetail.html', context)


def amazon(request):
    context = {
        'companyName': "Amazon"
    }
    return render(request, 'stockDetail.html', context)


def capgemini(request):
    context = {
        'companyName': "Capgemini"
    }
    return render(request, 'stockDetail.html', context)
