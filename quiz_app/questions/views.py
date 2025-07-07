from django.shortcuts import render
from django.http import HttpResponse

# HttpResponse - return input onto webpage

def questions(request):
    return HttpResponse("Hello world!")