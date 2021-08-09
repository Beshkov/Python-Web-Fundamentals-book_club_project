from django.shortcuts import render

from book_club.core.profile_utils import get_profile


def home(request):
    profile = get_profile()
    if profile:
        pass
    else:
        return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def log_in(request):
    pass

def create_profile(request):
    pass

def edit_profile(request, pk):
    pass

def view_profile(request, pk):
    pass

def delete_profile(request, pk):
    pass

