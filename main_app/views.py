from django.shortcuts import render
from django.http import HttpResponse
import time
import threading

# Create your views here.

def home(request):
    return render(request, 'about.html')

def countdown(n) :
    while n > 0:
        print (n)
        n = n - 1
        if n ==0:
            print('BLAST OFF!')


def gfg():
    print("good morning\n")

timer = threading.Timer(10.0, gfg)
timer.start()
print('good night\n')

countdown(5)



# calculate 24 hours into seconds
# learn how to call twilio into app
    # insert twilio call into timer.start()
