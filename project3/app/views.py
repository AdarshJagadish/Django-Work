from django.shortcuts import render
from django.http import HttpResponse

def index(request,data):
    return HttpResponse(data)

# Create your views here.
