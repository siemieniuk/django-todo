from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, NewTaskForm, RegisterForm
from .models import Task

# Create your views here.
def index_view(request):
    return render(
        request,
        'index.html'
    )

def dashboard_view(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(author = request.user.id)
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
    return redirect(index_view)

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
                return redirect(dashboard_view)

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
    else:
        form = RegisterForm()
    return render(
        request,
        'register.html',
        {
            'form': form
        }
    )