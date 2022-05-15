from tkinter.messagebox import RETRY
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def home(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def ticker(request):
    return render(request, 'ticker.html')

@login_required(login_url='login')
def stockDetails(request):
    return render(request,'stockDetails.html')

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
