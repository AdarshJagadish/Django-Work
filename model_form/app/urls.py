from django.urls import path
from . import views

urlpatterns = [
    path('',views.model_form_dis),
    path('media',views.uploadfile),
]
