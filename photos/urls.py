# from django.conf.urls import url
from importlib.resources import path
from . import views
from django.urls import path, re_path as url

# from django.urls import re_path, include

urlpatterns=[
    url(r'^$',views.gallery,name='gallery'),
    path('photo/<str:pk>/',views.viewPhoto, name='photo'),
    url('add/', views.addPhoto, name='add'),
     

]