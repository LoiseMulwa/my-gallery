# from django.conf.urls import url
from . import views
from django.urls import re_path
from django.urls import include, re_path

urlpatterns=[
    re_path('^$',views.welcome,name = 'welcome'),
]