from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else: 
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('login')
