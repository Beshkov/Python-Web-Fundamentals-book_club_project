from django.shortcuts import render, redirect

from book_club.core.profile_utils import get_profile
from book_club.user_profile.forms import UserProfileForm


def home(request):
    profile = get_profile()
    if profile:
        pass
    else:
        return render(request, 'home.html')


#TODO move about and log_in into a comman app.
def about(request):
    return render(request, 'about.html')

def log_in(request):
    pass

def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'user_templates/create-profile.html', context)

def edit_profile(request, pk):
    pass

def view_profile(request, pk):
    pass

def delete_profile(request, pk):
    pass

