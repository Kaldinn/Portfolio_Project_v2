from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .models import *
from .forms import *

# Create your views here.


def home_page(request):
    return render(request, 'mainsite/index.html')

def weather_app(request):
    return render(request, 'mainsite/weather.html')

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/tasks')
        else:
            messages.info(request, "Username or password are inncorect!")

    return render(request, 'mainsite/login.html')


def register_page(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {user}')
            
            return redirect('/login')
    context = {'form': form}

    return render(request, 'mainsite/register.html', context)

@login_required
def task_page(request):
    tasks = Task.objects.all()          #Pobiera wszystkie obiekty Task z bazy danych
    
    form = TaskForm()

    if request.method == 'POST':        #Sprawdzanie czy jest żadanie typu POST
        form = TaskForm(request.POST)   #Przypisanie do zmiennej dane z żadania POST jako argument
        if form.is_valid():             #Sprawdzainie czy przeszło walidacje
            form.save()                 #Zapisuje dane w bazie danych
        return redirect('/tasks')         

    context = {
        'tasks': tasks,
        'form': form     
    }
    return render(request, 'mainsite/task.html', context)

@login_required
def update_task(request, pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/tasks')

    context = {
        'form' : form
    }

    return render(request, 'mainsite/update_task.html', context)

@login_required
def delete_task(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect("/tasks")

    context = {
        "item": item
    }

    return render(request, 'mainsite/delete.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')