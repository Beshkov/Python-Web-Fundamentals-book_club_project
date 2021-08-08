from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Book_club.user_profile.urls')),
    path('events/', include('Book_club.events.urls')),
    path('books/', include('Book_club.book.urls')),
]
