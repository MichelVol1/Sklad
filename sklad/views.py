from django.shortcuts import render, redirect
from pyexpat.errors import messages

from .models import Iteam
from .forms import CreateUserForm, LoginForm, CreateTaskForm, UpdateUserForm
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context=context)


def login(request):
    form = LoginForm(request, data=request.POST)

    if form.is_valid():

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)

            return redirect("create_iteam")

    context = {'form': form}
    return render(request, 'login.html', context=context)


def logout(request):
    auth.logout(request)
    return redirect("login")


@login_required(login_url='login')
def createIteam(request):
    form = CreateTaskForm()

    if request.method == 'POST':

        form = CreateTaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)

            task.user = request.user

            task.save()

            return redirect('view_iteam')

    context = {'form': form}

    return render(request, 'create_iteam.html', context=context)


@login_required(login_url='login')
def viewIteam(request):
    current_user = request.user.id

    task = Iteam.objects.all().filter(user=current_user)

    context = {'task': task}

    return render(request, 'view-iteam.html', context=context)


@login_required(login_url='login')
def updateIteam(request, pk):
    task = Iteam.objects.get(id=pk)

    form = CreateTaskForm(instance=task)

    if request.method == 'POST':

        form = CreateTaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

            return redirect('view_iteam')

    context = {'form': form}

    return render(request, 'update-iteam.html', context=context)


@login_required(login_url='login')
def deleteIteam(request, pk):
    task = Iteam.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()

        return redirect('view_iteam')

    return render(request, 'delete-iteam.html')
