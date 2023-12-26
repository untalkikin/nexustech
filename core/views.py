from django.shortcuts import render
from .models import Service, Content

# Create your views here.

def home(request):
    contents = Content.objects.all()
    services = Service.objects.all()
    return render(request, "core/home.html", {'services' :services, 'contents' : contents})




