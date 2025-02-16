from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login as auth_login
from .forms import LoginForm
from .models import User  # Adjust to your app's name


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Check if user exists
            user = User.objects.filter(email=email).first()

            if user and check_password(password, user.password):
                # Redirect to home page on successful login
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def login_without_session(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Check if user exists
            user = User.objects.filter(email=email).first()

            if user and check_password(password, user.password):  # Manually check password
                return redirect('home')  # Redirect to the home page
            else:
                messages.error(request, 'Invalid credentials')  # Show error message

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def login_with_session(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Check if user exists
            user = User.objects.filter(email=email).first()

            if user and check_password(password, user.password):
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def home_view(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        return render(request, 'home.html', {'user': user})
    return redirect('login')


def logout_view(request):
    request.session.flush()
    return redirect('login')