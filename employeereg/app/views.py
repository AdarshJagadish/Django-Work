from django.shortcuts import render,redirect
from .models import *

# Create your views here.

adminid='admin'
adminpass='admin'
def adminlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if username==adminid and password==adminpass:
            request.session['adm']=username            
            return redirect(adminhome)
    return render(request,'login.html')

def adminhome(request):
    if 'adm' in request.session:
        return render(request,'home.html')
    else:
        return render(request,'login.html')

def userreg(request):
    return render(request,'register.html')