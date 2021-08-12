from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from book_club.book_event.forms import BookEventForm, EditBookEventForm
from book_club.book_event.models import BookEvent, Like, Dislike


def view_event(request, pk):
    book_ev = BookEvent.objects.get(pk=pk)
    book_ev.likes_count = book_ev.like_set.count()
    book_ev.dislikes_count = book_ev.dislike_set.count()

    context = {
        'book_ev': book_ev,
    }

    return render(request, 'book-events/view-book-event.html', context)


def all_events(requests):
    context = {
        'events': BookEvent.objects.all(),
    }

    return render(requests, 'book-events/all-events.html', context)


@login_required
def create_event(request):
    if request.method == "POST":
        form = BookEventForm(request.POST)
        if form.is_valid():
            club_event = form.save(commit=False)
            club_event.user = request.user
            club_event.save()
            return redirect('home')
    else:
        form = BookEventForm()

    context = {
        'form': form,
    }

    return render(request, 'book-events/create-book-event.html', context)


def book_event_details(request, pk):
    book_event = BookEvent.objects.get(pk=pk)

    is_owner = book_event.user == request.user

    context = {
        'book_event': book_event,
        'is owner': is_owner,
    }

    return render(request, 'book-events/view-book-event.html', context)


def edit_event(request, pk):
    club_event = BookEvent.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBookEventForm(request.POST, instance=club_event)
        if form.is_valid():
            form.save()
            return redirect('view book event', pk)
    else:
        form = EditBookEventForm(instance=club_event)

    context = {
        'club_event': club_event,
        'form': form,
    }

    return render(request, 'book-events/edit-book-event.html', context)


def delete_event(request, pk):
    pass


def like_event(request, pk):
    event_to_like = BookEvent.objects.get(pk=pk)
    like = Like(
        event=event_to_like,
    )
    like.save()
    return redirect('view book event', event_to_like.id)


def dislike_event(request, pk):
    event_to_dislike = BookEvent.objects.get(pk=pk)
    dislike = Dislike(
        event=event_to_dislike,
    )
    dislike.save()
    return redirect('view book event', event_to_dislike.id)
