from django.shortcuts import render
from django.http import HttpResponse
import datetime


def greeting(req):
    return HttpResponse("Hello from Customer App")

def get_time(req):
    message = "Current time in PST is "
    time = datetime.datetime.now()
    message+= time.strftime("%H:%M:%S")
    message += " on " + time.strftime("%Y-%m-%d")
    return HttpResponse(message)

def add_nums(req, num1, num2):
    result = num1 + num2
    message = "sum of "+ str(num1) + " and " + str(num2) + " is " + str(result)
    return HttpResponse(message)

def adding_by_get(req):

    result = int(req.GET["x"]) + int(req.GET["y"])
    message = "sum is " + str(result)
    return HttpResponse(message)
