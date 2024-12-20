from django.shortcuts import render,redirect
from .models import *
from .form import *
# Create your views here.

def model_form_dis(request):
    data=model_form()
    if request.method=='POST':
        form=model_form(request.POST)
        form.save()
        return redirect(model_form_dis)
    return render(request,'index.html',{'data':data})

def uploadfile(request):
    if request.method=='POST':
        file=request.FILES['file']
        description=request.POST['description']
        data=media.objects.create(file=file,description=description)
        # upload=media.objects.all()
        # print(file,description)
        # print(upload)
        data.save()
        return redirect(uploadfile)
    return render(request,'index2.html')