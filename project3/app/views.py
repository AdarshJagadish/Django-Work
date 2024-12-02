from django.shortcuts import render
from django.http import HttpResponse

users=[]

def index(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        print(name,email,password)
        users.append({'name':name,'email':email,'password':password})
        print(users)

    return render(request,'index.html',{'users':users})

def admin(request):
    return render(request,'admin.html')
    

# Create your views here.