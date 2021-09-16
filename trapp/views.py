from os import name
from django.db.models.fields import EmailField
from django.shortcuts import render, HttpResponse
from trapp.models import Dmdl


# Create your views here.
def index(request):
    if request.method =="POST":
        name =request.POST.get("name")
        email = request.POST.get("email")
        phoneno = request.POST.get("phoneno")
        Message = request.POST.get("Message")
        sdl = Dmdl(name=name, email=email, phoneno=phoneno, Message=Message)
        sdl.save()

    return render (request, 'index.html')


