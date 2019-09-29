from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.

def home(request):
    return render(request, 'about.html')

def countdown(n) :
    while n > 0:
        print (n)
        n = n - 1
        if n ==0:
            print('BLAST OFF!')


countdown(50)