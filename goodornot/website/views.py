
# Create your views here.
from django.shortcuts import render
from .models import Images,Comments


def listPictures(request):
    images = Images.objects.all()
    comments = []
    for image in images:
        curr = []
        

    return render(request,'main.html', {'image':Images.objects.all()}) 

    return render(request,'main.html', {'image':loadImages()}) 
def    loadImages():
 return Images.objects.all()


def loadComments():
 return Comments.objects.all()