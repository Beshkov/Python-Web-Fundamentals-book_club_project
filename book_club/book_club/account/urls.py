from django.urls import path
from book_club.account.views import sign_in, sign_up, sign_out, profile_details, delete_profile, user_library

urlpatterns = (
    path('sign-up/', sign_up, name='sign up'),
    path('sign-in/', sign_in, name='sign in'),
    path('sign-out/', sign_out, name='sign out'),
    path('user-profile', profile_details, name='view profile'),
    path('delete-user/', delete_profile, name='delete profile'),
    path('user-library/', user_library, name='user library')
)
