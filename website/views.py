from django.shortcuts import render
from .models import Images,Comments
def listPictures(request):
<<<<<<< HEAD
    return render(request, ‘pictures.html’, {image:Images.objects.all()}) 
=======
    return render(request, ‘pictures.html’, {image:loadImages()}) 
def    loadImages():
 return Images.objects.all()
>>>>>>> 6fee7dd02c0aad902ff9c254607605255c923290

def loadComments():
 return Comments.objects.all()
