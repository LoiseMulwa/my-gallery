
from multiprocessing import context
from tkinter import Image
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
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html' , context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html',{'photo': photo} )
    

def addPhoto(request):
    categories = Category.objects.all()

    # if request.method == 'POST':
    #     # data.request.POST
    #     image = request.FILES.get('image')

    #     # print('data:', data )
    #     # print('image:', image )
    context = {'categories': categories}
    return render(request,'photos/add.html', context)


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_photos = Category.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"categories": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})


