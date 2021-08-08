from django.urls import path

from Book_club.events.views import view_event, all_events, create_event

urlpatterns = (
    path('event/<int:pk>', view_event, name='view event'),
    path('all%20event/', all_events, name='all events'),
    path('create%20event/', create_event, name='create event'),
)
