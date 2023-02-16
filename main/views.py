from django.shortcuts import render, redirect
from . models import Pergunta, Resposta
from django.db.models import Q


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    pergunta = Pergunta.objects.filter(
        Q(topico__nome__icontains=q) |
        Q(descricao__icontains=q) |
        Q(corpo__icontains=q)
    )
    context = {'pergunta':pergunta}

    if request.method == 'GET':
        return render(request, 'main/home.html', context)
    

def pergunta(request, id):
    pergunta = Pergunta.objects.get(id=id)
    resposta = Resposta.objects.filter(Pergunta_id=id)
    context = {'pergunta':pergunta, 'resposta': resposta}

    if request.method == 'GET':
        return render(request, 'main/pergunta.html', context)
            