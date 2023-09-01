from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TaskForm, UserRegisterForm, UserLoginForm
from .models import Task
from django.contrib import messages


@login_required(login_url='login')
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form' : form, 'tasks' : tasks}
    return render(request, 'app1/main.html', context)


def delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('index')


def edit(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request, 'app1/edit.html', context)

def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Something went wrong during registration!')

    context = {'form':form}
    return render(request, 'app1/registration.html', context)


def user_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Wrong username or password!')
    context = {'form':form}
    return render(request, 'app1/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('index')