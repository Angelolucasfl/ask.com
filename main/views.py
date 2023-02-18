from django.shortcuts import render, redirect
from . models import Pergunta, Resposta, Topico
from django.db.models import Q
from . forms import PerguntaForm
from django.contrib import messages
from django.contrib.messages import constants


def home(request):
    topicos = Topico.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    pergunta = Pergunta.objects.filter(
        Q(topico__nome__icontains=q) |
        Q(descricao__icontains=q) |
        Q(corpo__icontains=q)
    )
    context = {'pergunta':pergunta, 'topicos':topicos}

    if request.method == 'GET':
        return render(request, 'main/home.html', context)
    

def perguntar(request):
    form = PerguntaForm()
    topicos = Topico.objects.all()
    context = {'form':form, 'topicos':topicos}


    if request.method == "GET":
        return render(request, 'main/pergunta_form.html', context)
    
    elif request.method == 'POST':
        nome_topico = request.POST.get('topico')
        topico, created = Topico.objects.get_or_create(nome=nome_topico)

        Pergunta.objects.create(
            host = request.user,
            topico = topico,
            corpo = request.POST.get('corpo'),
            descricao = request.POST.get('descricao'),
        )
        return redirect('home')
        

def editar_pergunta(request, id):
    pergunta = Pergunta.objects.get(id=id)
    form = PerguntaForm(instance=pergunta)
    topicos = Topico.objects.all()
    context = {'form':form, 'topcios':topicos, 'pergunta':pergunta}

    if request.method == "GET":
        print(pergunta)
        return render(request, 'main/pergunta_form.html', context)
    
    elif request.method == "POST":
        nome_topico = request.POST.get('topico')
        topico, created = Topico.objects.get_or_create(nome=nome_topico)

        pergunta.corpo = request.POST.get('corpo')
        pergunta.topico = topico
        pergunta.descricao = request.POST.get('descricao')
        pergunta.save()

        return redirect('home')


def deletar(request, id):
    pergunta = Pergunta.objects.get(id=id)

    if request.user != pergunta.host:
        messages.add_message(request, constants.ERROR, 'Você não pode apagar essa pergunta!')
        return redirect('pergunta', pergunta.id)

    if request.method == "GET":
        return render(request, 'main/delete.html', {'obj':'pergunta'})
    
    elif request.method == "POST":
        pergunta.delete()
        return redirect('home')
    

def pergunta(request, id):
    pergunta = Pergunta.objects.get(id=id)
    resposta = pergunta.resposta_set.all()
    context = {'pergunta':pergunta, 'resposta': resposta}

    if request.method == 'GET':
        return render(request, 'main/pergunta.html', context)
    

    elif request.method == 'POST':
        resposta = Resposta.objects.create(
            usuario = request.user,
            Pergunta = pergunta,
            corpo = request.POST.get('resposta')
        )

        return redirect('pergunta', id = pergunta.id)


def deletar_resposta(request, id):
    resposta = Resposta.objects.get(id=id)

    if request.user != resposta.usuario:
        messages.add_message(request, constants.ERROR, 'Você não pode apagar essa resposta!')
        return redirect('pergunta', pergunta.id)

    if request.method == "GET":
        return render(request, 'main/delete.html', {'obj': 'resposta'})
    
    elif request.method == "POST":
        resposta.delete()
        return redirect('home')
    

def topicos(request):
    return render(request, 'main/topicos.html')
