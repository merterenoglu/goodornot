from django.shortcuts import render
from .models import Images,Comments
def listPictures(request):
    return render(request, ‘pictures.html’, {image:’image’}) 
def    loadImages():
 imagesHTML = ""
 for image in Image.objects.all():
    imagesHTML += '<img src="'+image.idl+'">'
 return imagesHTML

# Create your views here.
