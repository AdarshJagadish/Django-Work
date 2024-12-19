from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def userform(request):
    data=user_form()
    if request.method=='POST':
        form=user_form(request.POST)
        if form.is_valid():
            roll=form.cleaned_data['roll']
            name=form.cleaned_data['name']
            mark=form.cleaned_data['mark']
            data1=student.objects.create(roll=roll,name=name,mark=mark)
            data1.save()
    return render(request,'index.html',{'data':data})