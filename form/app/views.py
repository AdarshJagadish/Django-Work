from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def userform(request):
    data=user_form()
    return render(request,'index.html',{'data':data})