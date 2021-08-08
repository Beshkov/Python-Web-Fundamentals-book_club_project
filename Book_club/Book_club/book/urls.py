from django.urls import path

from Book_club.book.views import add_book, view_book, remove_book, edit_book

urlpatterns = (
    path('add/', add_book, name='add book'),
    path('view/<int:pk>', view_book, name='view book'),
    path('remove/<int:pk>', remove_book, name='remove book'),
    path('edit/<int:pk>', edit_book, name='edit book')
)
