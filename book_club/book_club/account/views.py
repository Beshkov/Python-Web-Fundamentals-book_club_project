from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DeleteView

from book_club.account.forms import SignInForm, ProfileForm, CreateProfileForm

from book_club.account.models import Profile, BookClubUser
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
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/sign_up.html', context)


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
            return redirect('view profile')
    else:
        form = ProfileForm(instance=profile)

    user_books = Book.objects.filter(user_id=request.user.id)

    context = {
        'form': form,
        'user_books': user_books,
        'profile': profile,
    }

    return render(request, 'accounts/user_profile.html', context)

@login_required
def delete_profile(request):
    profile = Profile.objects.get(pk=request.user.id)
    user = profile.user
    user_form = CreateProfileForm(instance=user)

    context = {
        'user_form': user_form,
        'profile': profile
    }
    if request.method == 'GET':

        return render(request, 'accounts/delete-profile.html', context)
    
    user.delete()
    profile.delete()
    return redirect('home')