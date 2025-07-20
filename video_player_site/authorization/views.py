from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('authorization:login')

    else:
        form = UserRegistrationForm()
    
    return render(request, 'authorization/registration.html', {'form' : form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('main:index')
        
    return render(request, 'authorization/login.html')

def logout_view(request):
    if request.user:
        logout(request)
        return redirect('main:index')
