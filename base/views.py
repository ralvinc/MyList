from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.db.models import Q

from .models import Task
from .forms import TaskForm

def loginUser(request):
    page = 'login'

    # If user is already logged in, restrict user from loginPage
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        # Check if user exists
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        # Authenticate user credentials
        user = authenticate(request, username=username, password=password)

        # Login and create session for user
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password is incorrect")
    
    return render(request, 'base/login_register.html', {
        'page': page,
    })

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    # If user is already logged in, restrict user from registerPage
    if request.user.is_authenticated:
        return redirect('home')

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            # Login user after registering
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occured during registration.")
            messages.error(request, "Your password can't be similar to your username.")
            messages.error(request, "Your password must contain at least 8 characters.")
            messages.error(request, "Your password can’t be entirely numeric.")
            
    return render(request, 'base/login_register.html', {
        'form': form,
    })

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    tasks = []
    task_total_count = 0
    watch_count = 0
    read_count = 0

    if request.user.is_authenticated:
        tasks = Task.objects.filter(
            user = request.user).filter(
                Q(name__icontains = q) |
                Q(note__icontains = q)
        )

        task_total_count = Task.objects.filter(user=request.user).count()
        watch_count = Task.objects.filter(user=request.user).filter(Q(watch_or_read__action='Watch') | Q(watch_or_read__action='Both')).filter(completed=False).count()
        read_count = Task.objects.filter(user=request.user).filter(Q(watch_or_read__action='Read') | Q(watch_or_read__action='Both')).filter(completed=False).count()

    return render(request, 'base/home.html', {
        'tasks': tasks,
        'task_total_count': task_total_count,
        'watch_count': watch_count,
        'read_count': read_count,
    })

@login_required(login_url='login')
def createTask(request):
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    
    return render(request, 'base/task_form.html', {
        'form': form,
    })

@login_required(login_url='login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    # Prefill form with existing data
    form = TaskForm(instance=task)  
    
    if request.user != task.user:
        return redirect('home')

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/task_form.html', {
        'form': form,
    })

@login_required(login_url='login')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.user != task.user:
        return redirect('home')

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {
        'task': task,
    })