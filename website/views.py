from django.shortcuts import render
from .models import Images,Comments
def listPictures(request):
<<<<<<< HEAD
    return render(request, ‘pictures.html’, {image:Images.objects.all()}) 
=======
    return render(request, ‘pictures.html’, {image:loadImages()}) 
def    loadImages():
 return Images.objects.all()


def loadComments():
 return Comments.objects.all()
