from django.urls import path
from book_club.account.views import sign_in, sign_up, sign_out

urlpatterns = (
    path('sign-up/', sign_up, name='sign up'),
    path('sign-in/', sign_in, name='sign in'),
    path('sign-out/', sign_out, name='sign out'),
)
