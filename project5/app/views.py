from django.shortcuts import render,redirect
from django.http import HttpResponse

users=[]

def register(request):
    if request.method=='POST':
        slno=len(users)
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        # print(slno,name,email,password)
        users.append({'slno':slno+1,'name':name,'email':email,'password':password})
        print(users)
        return redirect(login)
    return render(request,'register.html',{'users':users})

def login(request):
    message=''
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        for i in users:
            if i['email']==email and i['password']==password:
                message='Login Succesfull'
                return redirect(home)
            else:
                message='Invalid email or password'
    return render(request,'login.html',{'message':message})

def home(request):
    
    return render(request,'home.html')

adminuname="admin"
adminpass="admin@123"
def adminlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if username==adminuname and password==adminpass:
            print("logged in")
            return redirect(adminhome)
    return render(request,'adminlogin.html')
    
def adminhome(request):
    return render(request,'adminhome.html',{'users':users})

# Create your views here.