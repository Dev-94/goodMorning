from django.shortcuts import render
from django.http import HttpResponse
import time
import threading
# from twilio.rest import Client


# Create your views here.

def home(request):
    return render(request, 'about.html')

# def countdown(n) :
#     while n > 0:
#         print (n)
#         n = n - 1
#         if n ==0:
#             print('BLAST OFF!')

#sends sms message adn prints goodnight
def gfg():
    print("good morning\n")
    from send_sms import message    
    print('good night\n')

#establishes paramaters for timer
timer = threading.Timer(10.0, gfg)

#call timer to begin
timer.start()

# print(Client)


# countdown(5)



# calculate 24 hours into seconds
    # sms is inserted into gfg timer function

        #calculate timer to 24 hours and attach it to server

        #later attach API that is iterated and texted through
