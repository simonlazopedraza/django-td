from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ContactFormForm

def index(request) -> HttpResponse:
    flanes = Flan.objects.filter(is_private=False)
    context = {
        'productos' : flanes
    }
    return render(request, 'index.html', context)

def about(request) -> HttpResponse:
    context = {}
    return render(request, 'about.html')

@login_required
def welcome(request) -> HttpResponse:
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'nombre_usuario': request.user.username,
        'flanes_privados' : flanes_privados
    }
    return render(request, 'welcome.html', context)

def contact(request) -> HttpResponse:
    if request.method == 'POST':
        formulario = ContactFormForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('success') 
    else:
        formulario = ContactFormForm()
    context = {'formulario': formulario}
    return render(request, 'contact.html', context)

def success(request) -> HttpResponse:
    return render(request, 'success.html')