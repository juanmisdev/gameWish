from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib import messages

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # login user:
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            messages.success(request, f'Bienvenido a GameWish {username}!')
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # login user:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Bienvenido a GameWish {username}!')
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return render(request, 'login.html', )
    else:
        return render(request, 'login.html', )

def logout(request):
    auth_logout(request)
    messages.success(request, 'Has cerrado sesión.')
    return redirect('home')