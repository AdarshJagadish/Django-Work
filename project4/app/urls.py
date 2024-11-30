from django.urls import path
from . import views
urlpatterns=[
    path('index/<int:data1>/<int:data2>',views.index)
]