from django.shortcuts import render,redirect
from django.http import HttpResponse

users=[]

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        print(name,email,password)
        users.append({'name':name,'email':email,'password':password})
        return redirect(login)
    return render(request,'register.html',{'users':users})

def login(request):
    return render(request,'login.html')

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