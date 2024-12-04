from django.urls import path
from . import views
urlpatterns=[
    path('',views.login),
    path('userregister',views.register),
    path('adminlogin',views.adminlogin),
    path('adminhome',views.adminhome),
    path('userhome',views.home),
]