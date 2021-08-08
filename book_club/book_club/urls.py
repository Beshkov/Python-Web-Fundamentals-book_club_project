from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book_club.user_profile.urls')),
    path('events/', include('book_club.book_event.urls')),
    path('books/', include('book_club.book.urls')),
]
