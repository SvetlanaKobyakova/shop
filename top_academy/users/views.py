from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegistrationForm, ProfileForm


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f'{user.username}, Вы успешно зарегистрировались и вошли!!')
            return HttpResponseRedirect(reverse('main:index'))

    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'users/registration.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f'{username}, Вы вошли на сайт')

            return HttpResponseRedirect(reverse('main:index'))

    else:
        form = UserLoginForm()

    context = {
        'form': form
    }

    return render(request, 'users/login.html', context)


@login_required
def logout(request):
    messages.success(request, f'{request.user.username}, Вы вышли')
    auth.logout(request)

    return redirect(reverse('main:index'))


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные обновлены')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, 'users/profile.html', context)