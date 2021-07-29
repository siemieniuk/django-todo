from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, NewTaskForm, RegisterForm
from .models import Task

# Create your views here.
def index_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(
            request,
            'index.html'
        )

def dashboard_view(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(author=request.user.id)
        newtaskform = NewTaskForm()
        return render(
            request,
            'dashboard.html',
            {
                'user': request.user,
                'tasks': tasks,
                'newtaskform': newtaskform,
            }
        )
    return redirect('index')

def create_task_view(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = NewTaskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['title']
            task = Task(name=name, author=request.user)
            task.save()
        return redirect(dashboard_view)

def delete_task_view(request):
    if request.method == 'GET' and request.user.is_authenticated:
        pass


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')

    return render(
        request,
        'login.html',
        {
            'form': form,
        }
    )

def logout_view(request):
    logout(request)
    return redirect('index')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(
        request,
        'register.html',
        {
            'form': form
        }
    )