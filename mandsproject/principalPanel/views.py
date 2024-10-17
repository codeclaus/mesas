from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroUsuarioForm
# Create your views here.
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from shoppcar.car import ShoppCar
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    car = ShoppCar(request)
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            # Redirige a la página principal después del registro
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'register.html', {'form': form})


def register2(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            # Redirige a la página principal después del registro
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'home.html', {'form': form})


def logear(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                # Redirige a la página principal después del inicio de sesión
                return redirect('home')
            else:
                messages.error(request, "ingresa algo valido")
                # Redirige a la página principal después del inicio de sesión
        else:
            messages.error(request, "eso no es valido")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logear2(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'home.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirige a la página principal después del login
                return redirect('home')
            else:
                # Autenticación fallida
                return render(request, 'home.html', {'form': form, 'error': 'Credenciales inválidas'})

        # Formulario inválido
        return render(request, 'home.html', {'form': form})


def close_sesion(request):
    logout(request)
    return redirect("home")


def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Enviar el correo
        subject = f"Nuevo mensaje de {name}"
        email_message = f"Nombre: {name}\nEmail: {
            email}\n\nMensaje:\n{message}"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['jhonbtm1998@gmail.com']  # Cambia esto por tu correo

        send_mail(subject, email_message, from_email, recipient_list)

        # Redirigir a una página de éxito
        return redirect('success')

    # Si no es POST, redirigir al formulario
    return redirect('home')


def success(request):
    return render(request, 'success.html')
