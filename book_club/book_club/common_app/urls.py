from django.urls import path

from book_club.common_app.views import HomePageView, AboutPageView

urlpatterns = (
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
)
