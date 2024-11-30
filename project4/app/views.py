from django.shortcuts import render
from django.http import HttpResponse

def index(request,data1,data2):
    product=data1*data2
    result=data1+data2
    return HttpResponse('Product = '+str(product)+'<br> Sum = '+str(result))


# Create your views here.
