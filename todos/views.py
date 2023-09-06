from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.


def home(request):
    return render(request, "todos/home.html")

def carrinho(request):
    return render(request, "todos/carrinho.html")

def registrar(request):
    
    return render(request, "todos/registrar.html")