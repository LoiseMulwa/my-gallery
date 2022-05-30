
from multiprocessing import context
# from tkinter import PhotoImage
from unicodedata import category
from django.shortcuts import render



from .models import Category, Photo
# from django.http  import HttpResponse


# Create your views here.
# def put(self, request, *args, **kwargs):
# def gallery(request, self, *args, **kwargs):
    # pk = self.kwargs.get('pk')
def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)


    categories = Category.objects.all()
    # photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html' , context)

def viewPhoto(request):
    photo = Photo.objects.all()
    return render(request, 'photos/photo.html',{'photos': photo} )
    

def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        # data.request.POST
        image = request.FILES.get('image')

        # print('data:', data )
        # print('image:', image )

        


    context = {'categories': categories}
    return render(request,'photos/add.html', context)


