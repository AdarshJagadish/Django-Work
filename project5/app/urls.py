from django.urls import path
from . import views
urlpatterns=[
    path('',views.register),
    path('adminlogin',views.adminlogin),
    path('adminhome',views.adminhome),
    path('userlogin',views.login),
    path('userhome',views.home),
]