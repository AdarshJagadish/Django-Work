from django.shortcuts import render,redirect
from django.http import HttpResponse

users=[]

def index(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        print(name,email,password)
        users.append({'name':name,'email':email,'password':password})
        return redirect(adminhome)
    return render(request,'index.html',{'users':users})


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
    return render(request,'adminhome.html')

# Create your views here.