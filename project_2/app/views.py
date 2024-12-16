from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.utils import timezone

# Create your views here.
def userregister(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        data=User.objects.create_user(first_name=name,username=username,email=email,password=password)
        data.save
        return redirect(userlogin)
    return render(request,'user/register.html')

def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        current_time=timezone.now()
        
        user=auth.authenticate(username=username,password=password,last_login=current_time)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect(userhome)
    return render(request,'user/login.html')

def userhome(request):
    if '_auth_user_id' in request.session:
        user=User.objects.get(pk=request.session['_auth_user_id'])
        return render(request,'user/home.html')
    else:
        return redirect(userlogin)

def userlogout(request):
    if '_auth_user_id' in request.session:
        auth.logout(request)
        return redirect(userlogin)

adminid='admin'
adminpass='admin'
def adminlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password'] 
        if username==adminid and password==adminpass:
            request.session['adm']=username            
            return redirect(adminhome)
    return render(request,'admin/login.html')

def adminhome(request):
    if 'adm' in request.session:
        user=User.objects.all()
        return render(request,'admin/home.html',{'user':user})
    else:
        return render(request,'admin/login.html')
    
def adminlogout(request):
    if 'adm' in request.session:
        del request.session['adm']
        return redirect(adminlogin)
    else:
        return redirect(adminlogin)