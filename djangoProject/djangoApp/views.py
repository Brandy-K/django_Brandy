from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import User


def login_view(request):
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.filter(email=email, password=password).first()
            if user:
                return render(request, 'home.html', {'user': user})
            else:
                message = "Invalid credentials"
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'message': message})


def login_with_session(request):
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.filter(email=email, password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect('home')
            else:
                message = "Invalid credentials"
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'message': message})



