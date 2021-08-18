import os
from os.path import join

from django.conf import settings
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, FormView

from book_club.account.forms import SignInForm, ProfileForm, CreateProfileForm, EditProfileForm

from book_club.account.models import Profile, BookClubUser
from book_club.book.models import Book
from book_club.book_event.models import BookEvent

# PasswordChangeForm #TODO implement password


def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignInForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/sign_in.html', context)


def sign_up(request):
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/sign_up.html', context)


def sign_out(request):
    logout(request)
    return redirect('home')

#
# class ProfileDetailsView(LoginRequiredMixin, FormView):
#     template_name = 'accounts/user_profile.html'
#     form_class = ProfileForm
#     success_url = reverse_lazy('view profile')
#     object = None
#
#     def get(self, request, *args, **kwargs):
#         self.object = Profile.objects.get(pk=request.user.id)
#         return super().get(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         self.object = Profile.objects.get(pk=request.user.id)
#
#     def form_valid(self, form):
#         self.object.profile_image = form.cleaned_data['profile_image']
#         self.object.save()
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['book'] = Book.objects.filter(user_id=self.request.user.id)
#         context['book_event'] = BookEvent.objects.filter(user_id=self.request.user.id)
#         context['profile'] = self.object
#
#         return context

# class EditUserProfile(LoginRequiredMixin, UpdateView):
#     model = Profile
#     template_name = 'accounts/edit-user-profile.html'
#     form_class = EditProfileForm
#     success_url = reverse_lazy('view profile')
#

@login_required
def profile_details(request):

    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )
        if form.is_valid():
            form.save()

            return redirect('view profile')
    else:
        form = ProfileForm(instance=profile)

    user_books = Book.objects.filter(user_id=request.user.id)

    context = {
        'form': form,
        'user_books': user_books,
        'profile': profile,
    }

    return render(request, 'accounts/user_profile.html', context)

@login_required
def delete_profile(request):
    profile = Profile.objects.get(pk=request.user.id)
    user = profile.user
    user_form = CreateProfileForm(instance=user)

    context = {
        'user_form': user_form,
        'profile': profile
    }
    if request.method == 'GET':

        return render(request, 'accounts/delete-profile.html', context)

    user.delete()
    profile.delete()

    return redirect('home')
