from email.mime import image
from unicodedata import category
from django.db import models

import photos

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(name__icontains=search_term)
        return photos


    def __str__(self):
        return self.name



class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    photo = models.ImageField(max_length=500, null=False, blank=False)



    def __str__(self):
        return self.description


