from django.urls import path

from book_club.book_event.views import view_event, all_events, create_event, delete_event, like_event, dislike_event

urlpatterns = (
    path('', all_events, name='all events'),
    path('book_event/<int:pk>', view_event, name='view book event'),
    path('delete-book-event/<int:pk>', delete_event, name='delete book event'),
    path('create-event/', create_event, name='create book event'),
    path('like/<int:pk>', like_event, name='like event'),
    path('dislike/<int:pk>', dislike_event, name='dislike event'),
)
