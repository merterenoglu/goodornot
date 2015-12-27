from django.shortcuts import render
from .models import Images,Comments


def listPictures(request):
    images = Images.objects.all()
    comments = []
    for image in images:
        curr = []
        curr.append(Comments.objects.get(idl=image.idl))

    return render(request,'pictures.html', {image:Images.objects.all(),comment:comments}) 

    return render(request,'pictures.html', {image:loadImages()}) 
def    loadImages():
 return Images.objects.all()


def loadComments():
 return Comments.objects.all()
