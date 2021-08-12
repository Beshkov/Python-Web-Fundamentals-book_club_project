from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from book_club.account.forms import SignInForm, ProfileForm

from book_club.account.models import Profile
from book_club.book.models import Book


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


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)

    user_books = Book.objects.filter(user_id=request.user.id)

    context = {
        'form': form,
        'user_books': user_books,
        'profile': profile,
    }

    return render(request, 'accounts/user_profile.html', context)