from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse  # Поможет использовать ссылки по их name -> Адрес

from users.models import User
from users.forms import UserLoginForm


def login(request):
    """Login controller"""
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)  # Если пользователь есть - он авторизуется
                return HttpResponseRedirect(reverse('index'))

    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    """Registration controller"""
    return render(request, 'users/registration.html')
