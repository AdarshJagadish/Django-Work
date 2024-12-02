from django.urls import path
from . import views
urlpatterns=[
    path('index1/<int:data>',views.index),
    path('index2',views.index2),
]