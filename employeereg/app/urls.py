from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminlogin),
    path('home',views.adminhome),
    path('register',views.userreg),
]