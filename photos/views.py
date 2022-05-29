from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from .models import Category, Photo
# from django.http  import HttpResponse


# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'photos/gallery.html')

def viewPhoto(request):
    return render(request,'photos/photo.html')

def addPhoto(request):
    return render(request,'photos/add.html')


