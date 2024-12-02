from django.shortcuts import render
from django.http import HttpResponse

user=[]

def index(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        print(name,email,password)
        user.append({'name':name,'email':email,'password':password})
        print(user)

    return render(request,'index.html')

def admin(request):
    return render(request,'admin.html')
    

# Create your views here.