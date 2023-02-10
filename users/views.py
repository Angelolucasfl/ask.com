from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required


def cadastrar(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "GET":
        return render(request, 'users/login.html')
    
    elif request.method == "POST":
        nome_usuario = request.POST.get('nome_usuario')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

    
        if len(nome_usuario.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos!')
            return render(request, 'users/login.html')

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Digite duas senhas iguais!')
            return render(request, 'users/login.html')

        try:
            user = User.objects.create_user(
                username=nome_usuario,
                password=senha,
            )
            messages.add_message(request, constants.SUCCESS, "Cadastro realizado com sucesso!")
            return redirect('/auth/perfil')
        
        except:
            messages.add_message(request, constants.ERROR, 'Erro ao tentar cadastrar')
            return render(request, 'users/login.html')



def logar(request):

    if request.user.is_authenticated:
        return redirect('/auth/perfil')

    page = 'login'
    context = {'page':page}
    if request.method == 'GET':
        return render(request, 'users/login.html', context)
    
    elif request.method == 'POST':
        nome_usuario = request.POST.get('nome_usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=nome_usuario, password=senha)

        if user is not None:
            login(request, user)
            return render(request, 'users/perfil.html')
        
        else:
            messages.add_message(request, constants.ERROR, "Usuário ou senha incorretos")
            return render(request, 'users/login.html', context)
        

@login_required(login_url="logar")
def perfil(request):
    return render(request, 'users/perfil.html')        


def sair(request):
    logout(request)
    return redirect('/auth/login')
