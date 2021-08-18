from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import PasswordChangeForm
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

@login_required
def edit_event(request, pk):
    """
    Edit view that check if the request method is -> POST and
    if the obj.instance creator is the same user from the request.
    if all is valid then
    """
    club_event = BookEvent.objects.get(pk=pk)
    if request.method == 'POST' and club_event.user == request.user:

        form = EditBookEventForm(request.POST, instance=club_event,)
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


@login_required
def delete_event(request, pk):
    club_event = BookEvent.objects.get(pk=pk)
    if request.method == "POST" and club_event.user == request.user:
        club_event.delete()
        return redirect('all events')
    else:
        context = {
            'club_event': club_event,
        }
        return render(request, 'book-events/delete-book-event.html', context)


def like_event(request, pk):
    event_to_like = BookEvent.objects.get(pk=pk)
    user_liked_it = event_to_like.like_set.filter(user_id=request.user.id).first()
    if user_liked_it:
        user_liked_it.delete()
    else:
        like = Like(
            event=event_to_like,
            user=request.user,
        )
        like.save()
    return redirect('view book event', event_to_like.id)


def dislike_event(request, pk):
    event_to_dislike = BookEvent.objects.get(pk=pk)
    user_disliked_it = event_to_dislike.dislike_set.filter(user_id=request.user.id).first()
    if user_disliked_it:
        user_disliked_it.delete()
    else:
        dislike = Dislike(
            event=event_to_dislike,
            user=request.user,
        )
        dislike.save()
    return redirect('view book event', event_to_dislike.id)
