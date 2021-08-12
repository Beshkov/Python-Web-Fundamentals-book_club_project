from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

from book_club.account.forms import SignInForm


def sign_in(request):
    if request.method == "POST":
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

    return render(request, 'accounts/sign_in.html', context)


def sign_up(request):
    pass


def sign_out(request):
    logout(request)
    return redirect('home')




