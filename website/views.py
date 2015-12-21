from django.shortcuts import render
from .models import Images,Comments
def listPictures(request):
    return render(request, ‘pictures.html’, {image:loadImages()}) 
def    loadImages():
 return Images.objects.all().

