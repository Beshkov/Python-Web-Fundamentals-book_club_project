from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from book_club.book.forms import CreateBookForm, EditBookForm, DeleteBookForm
from book_club.book.models import Book

UserProfile = None

@login_required
def add_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('home')
    else:
        form = CreateBookForm()

    context = {
        'form': form,
    }

    return render(request, 'book_templates/add-book-to-collection.html', context)


def view_book(request, pk):
    book = Book.objects.get(pk=pk)

    book_owner = book.user == request.user

    context = {
        'book': book,
        'book_owner': book_owner,
    }

    return render(request, 'book_templates/book-details.html', context)


def remove_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    else:
        form = DeleteBookForm(instance=book)

    context = {
        'book': book,
        'form': form,
    }

    return render(request, 'book_templates/remove-book-from-collection.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('view book', pk)
    else:
        form = EditBookForm(instance=book)

    context = {
        'book': book,
        'form': form,
    }

    return render(request, 'book_templates/edit-book.html', context)