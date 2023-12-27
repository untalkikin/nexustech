from django.shortcuts import render
from .models import Service, Content, PictureUS, Partner

# Create your views here.

def home(request):
    contents = Content.objects.all()
    services = Service.objects.all()
    uspictures = PictureUS.objects.all() 
    partners = Partner.objects.all()
    return render(request, "core/home.html", {'services' :services, 'contents' : contents, 'uspictures' : uspictures, 'parters':partners})




