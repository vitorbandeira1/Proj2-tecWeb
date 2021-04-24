from django.shortcuts import render
from .models import TextField



def index(request):
    return render(request, 'moviegenerator/teste.html')