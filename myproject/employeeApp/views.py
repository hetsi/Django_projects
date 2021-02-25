from django.shortcuts import render
from django.http import HttpResponse

def greeting(req, name):
    message = "Hello "
    message += name + " ! "
    message += "from employee app <h2>"
    return HttpResponse(message)

# Create your views here.
