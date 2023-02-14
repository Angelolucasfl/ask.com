from django.shortcuts import render, redirect
from . models import Pergunta, Resposta


def home(request):
    pergunta = Pergunta.objects.all()
    context = {'pergunta':pergunta}

    if request.method == 'GET':
        return render(request, 'main/home.html', context)
    

def pergunta(request, id):
    pergunta = Pergunta.objects.get(id=id)
    resposta = Resposta.objects.get(Pergunta_id=id)
    context = {'pergunta':pergunta, 'resposta': resposta}

    if request.method == 'GET':
        return render(request, 'main/pergunta.html', context)