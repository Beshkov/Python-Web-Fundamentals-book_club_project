from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from book_club.book_club_auth.forms import SignInForm


def sign_up(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = UserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'auth/sign-up.html', context)


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    else:
        form = SignInForm()

    context = {
        'form': form,
    }

    return render(request, 'auth/sign-in.html', context)


def sign_out(request):
    logout(request)
    return redirect('home')
