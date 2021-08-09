from django.urls import path

from book_club.book_event.views import view_event, all_events, create_event, delete_event

urlpatterns = (
    path('book_event/<int:pk>', view_event, name='view book event'),
    path('delete-book-event/<int:pk>', delete_event, name='delete book event'),
    path('all-event/', all_events, name='all events'),
    path('create-event/', create_event, name='create book event'),
)
