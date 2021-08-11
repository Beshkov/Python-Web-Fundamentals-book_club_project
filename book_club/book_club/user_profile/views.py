from django.shortcuts import render, redirect

from book_club.book.models import Book
from book_club.core.profile_utils import get_profile
from book_club.user_profile.forms import UserProfileForm, EditProfileForm
from book_club.user_profile.models import UserProfile


def home(request):
    profile = get_profile()
    if profile:

        context = {
            'books':Book.objects.all()
        }

        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')


# TODO move about and log_in into a common app.
def about(request):
    return render(request, 'about.html')


def log_in(request):
    pass


def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'user_templates/create-profile.html', context)


def edit_profile(request, pk):
    user = UserProfile.objects.get(pk=pk)
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('all events')
    else:
        form = EditProfileForm(instance=user)

    context = {
        'form': form,
        'user': user,
    }

    return render(request, 'user_templates/edit-profile.html', context)


def view_profile(request):
    user = UserProfile.objects.first()
    books = Book.objects.all()

    context = {
        'user': user,
        'books': books,
    }

    return render(request, 'user_templates/view-profile.html', context)


def delete_user_profile(request, pk):
    pass
