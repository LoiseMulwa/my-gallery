from multiprocessing import context
# from tkinter import PhotoImage
from unicodedata import category
from django.shortcuts import render


from .models import Category, Photo
# from django.http  import HttpResponse


# Create your views here.
# def put(self, request, *args, **kwargs):
def gallery(request, self, *args, **kwargs):
    pk = self.kwargs.get('pk')
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html' , context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html',{'photos': photo} )
    

def addPhoto(request):
    return render(request,'photos/add.html')


