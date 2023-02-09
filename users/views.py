from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def logar(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    
    elif request.method == 'POST':
        nome_usuario = request.POST.get('nome_usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=nome_usuario, password=senha)

        if user is not None:
            login(request, user)
            return redirect('admin/')
        else:
            return render(request, 'users/login.html')
