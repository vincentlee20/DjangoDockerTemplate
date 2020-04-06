
from django.urls import path
from . import helloworld, views

urlpatterns =[
    path('', views.index, name='index'),
    path('process', helloworld.process, name='helloworld')
]