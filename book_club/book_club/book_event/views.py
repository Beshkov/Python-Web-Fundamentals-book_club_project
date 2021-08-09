from django.shortcuts import render, redirect

from book_club.book_event.models import BookEvents, Like, Dislike


def view_event(request, pk):
    pass

def all_events(requests):
    pass

def create_event(request):
    pass

def delete_event(request):
    pass

def like_event(request, pk):
    event_to_like = BookEvents.objects.get(pk=pk)
    like = Like(
        event=event_to_like,
    )
    like.save()
    return redirect('', event_to_like.id)

def dislike_event(request, pk):
    event_to_dislike = BookEvents.objects.get(pk=pk)
    dislike = Dislike(
        event=event_to_dislike,
    )
    dislike.save()
    return redirect('', event_to_dislike.id)
