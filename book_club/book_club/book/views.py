from django.shortcuts import render, redirect

from book_club.book.forms import CreateBookForm
from book_club.book.models import Book
from book_club.user_profile.models import UserProfile


def add_book(request):
    user = UserProfile.objects.first()
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateBookForm()

    context = {
        'form': form,
        'user': user
    }

    return render(request, 'book_templates/add-book-to-collection.html', context)


def view_book(request, pk):
    book = Book.objects.get(pk=pk)

    context = {
        'book': book
    }

    return render(request, 'book_templates/book-details.html', context)


def remove_book(request, pk):
    pass


def edit_book(request, pk):
    pass
