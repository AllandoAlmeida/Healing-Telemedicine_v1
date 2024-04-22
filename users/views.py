from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.messages import constants
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def register(request):
    if request.method == "GET":        
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem.')
            return redirect('/users/register')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve ter pelo menos 6 caracteres.')
            return redirect('/users/register')
        
        users = User.objects.filter(username=username)
        
        if users.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse us.')
            return redirect('/users/register')
        
        try:  # Tente criar o usuário
            user = User.objects.create_user(
                username=username,
                email=email,
                password=senha
            )
            messages.add_message(request, constants.SUCCESS, "Usuário cadastrado com sucesso")
        
            return redirect('/users/login')
        except IntegrityError:
            messages.add_message(request, constants.ERROR, 'O nome de usuário ou email já existe.')
            return redirect('/users/register')
        except Exception as e:  # Lidar com outros erros
            messages.add_message(request, constants.ERROR, 'Erro ao criar usuário: {}'.format(e))
            return redirect('/users/register')
        
        
def login_view(request):
    if request.method == "GET":        
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = auth.authenticate(request, username=username, password=senha)
        
        if user:
            auth.login(request, user)
            return redirect('/pacientes/home')
        
        messages.add_message(request, constants.ERROR, 'Credenciais inválidas, entre com credenciais validas')
        return redirect('/users/login')
    

def logout(request):
    auth.logout(request)
    print(request.user)
    return redirect('/users/login')