from django.shortcuts import render,redirect
from .models import *
from .form import *
# Create your views here.

def user_form_dis(request):
    data=user_form()
    if request.method == 'POST':
        form=user_form(request.POST)
        if form.is_valid():
            roll=form.cleaned_data['roll']
            name=form.cleaned_data['name']
            mark=form.cleaned_data['mark']
            data1=student.objects.create(roll=roll,name=name,mark=mark)
            data1.save()
    return render(request,'',{'data':data})

def model_form_dis(request):
    data=model_form()
    if request.method=='POST':
        form=model_form(request.POST)
        form.save()
        return redirect(model_form_dis)
    
    return redirect(request,'index.html',{'data':data})