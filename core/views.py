from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Evento
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def evento(request, nome):
    eve = Evento.objects.get(titulo=nome)
    return HttpResponse('<h1>{}</h1>'.format(eve))


@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    dados = Evento.objects.filter(usuario=usuario)
    # dados = Evento.objects.all()
    return render(request, 'agenda.html', {'eventos': dados})


def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuario ou senha incorretos!')
            return redirect('/')






def logout_user(request):
    logout(request)
    return redirect('/')