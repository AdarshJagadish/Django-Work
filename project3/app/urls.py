from django.urls import path
from . import views
urlpatterns=[
    path('index/<int:data1>',views.index)
]