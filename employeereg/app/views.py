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
    emps=employee.objects.all()
    deps=department.objects.all()
    if 'adm' in request.session:
        dep=request.POST['d']
        deppk=department.objects.all()
        return render(request,'home.html',{'deps':deps,'emps':emps})
    else:
        return render(request,'login.html')

def userreg(request):
    department=department.objects.all()
    if request.method=='POST':
        username=request.POST['username']
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        dep=request.POST['d']
        current_dep=department.objects.get(pk=dep)
        data=employee.objects.create(username=username,name=name,email=email,password=password)
        data.save()
        return redirect(adminlogin)
    return render(request,'register.html',{'deps':department})
        
def logout(request):
    if 'adm' in request.session:
        return redirect(adminlogin)
    else:
        return redirect(adminlogin)