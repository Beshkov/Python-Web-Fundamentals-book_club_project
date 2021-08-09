from django.urls import path

from book_club.user_profile.views import home, create_profile, edit_profile, view_profile, delete_profile, log_in, about

urlpatterns = (
    path('', home, name='home'),
    path('about', about, name='about'),
    path('login/', log_in, name='log in'),  # TODO implement
    path('profile/crate', create_profile, name='create profile'),
    path('profile/edit/<int:pk>', edit_profile, name='edit profile'),
    path('profile/view/<int:pk>', view_profile, name='view profile'),
    path('profile/delete/<int:pk>', delete_profile, name='delete profile'),

)
