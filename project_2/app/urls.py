from django.urls import path
from . import views

urlpatterns = [
    path('',views.userlogin),
    path('userregister',views.userregister),
    path('userhome',views.userhome),
    path('adminlogin',views.adminlogin),
    path('adminhome',views.adminhome),
    path('userlogout',views.userlogout),
    path('adminlogout',views.adminlogout),
]