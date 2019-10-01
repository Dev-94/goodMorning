from django.shortcuts import render
from django.http import HttpResponse
import time
import threading
# from twilio.rest import Client

# Render Home Page
def home(request):
    return render(request, 'about.html')


# Function to detect if it is 6:00 AM each day
def time_of_day:
    return time.strftime("%H:%M:%S")

target_time = "6:00:00"

while True:
    while time_of_day() != target_time:
        time.sleep(.1)
    call_function()
    while time_of_day() == target_time:
        time.sleep(.1)


# Functions for timers and calling Twilio sms API
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
timer = threading.Timer(1.0, gfg)

#call timer to begin
timer.start()


# Ways of accessing time of the day

# gives me time in seconds, not sure how to quantify
# print(time.clock()) 

# gives me day, month, date, hour, minute, seconds, year
print(time.ctime(%X, %P, 6:00, AM))

# give locat time, but broken into seperate elements in a tuple
# print(time.localtime()) 

# print(Client)


# countdown(5)



# calculate 24 hours into seconds
    # sms is inserted into gfg timer function

        #calculate timer to 24 hours and attach it to server

        #later attach API that is iterated and texted through
