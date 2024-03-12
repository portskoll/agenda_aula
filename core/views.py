from django.http import HttpResponse
from django.shortcuts import render, redirect

from core.models import Evento


# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def evento(request, nome):
    eve = Evento.objects.get(titulo=nome)
    return HttpResponse('<h1>{}</h1>'.format(eve))


def lista_eventos(request):
    # usuario = request.user
    # dados = Evento.objects.filter(usuario=usuario)
    dados = Evento.objects.all()
    return render(request, 'agenda.html', {'eventos': dados})
