from django.urls import path

from book_club.book_event.views import view_event, all_events, create_event

urlpatterns = (
    path('book_event/<int:pk>', view_event, name='view book_event'),
    path('all%20event/', all_events, name='all events'),
    path('create%20event/', create_event, name='create book_event'),
)
