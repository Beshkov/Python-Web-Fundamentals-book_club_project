import os
from os.path import join
# from django.contrib.auth.forms import PasswordChangeForm
from django.conf import settings
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from book_club.account.forms import SignInForm, ProfileForm, CreateProfileForm, EditProfileForm

from book_club.account.models import Profile, BookClubUser
from book_club.book.models import Book


# PasswordChangeForm #TODO implement password change


# def sign_in(request):
#     if request.method == "POST":
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignInForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'accounts/sign_in.html', context)


class SignInView(LoginView):
    """
    if you gonna remove this view remove the LOGIN_REDIRECT_URL = 'home' at line 145 in settings.py the whole reason we
    place that there is so we can override the LOGIN_REDIRECT_URL = 'account/profile in global_settings.py file  """
    template_name = 'accounts/sign_in.html'
    authentication_form = SignInForm
    success_url = reverse_lazy('home')


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
        try:
            old_image_path = profile.profile_image.path
        except ValueError:
            old_image_path = False
            pass

        if form.is_valid():
            form.save(commit=False)

            # try:
            #     os.remove(old_image_path)
            # except FileNotFoundError and UnboundLocalError :
            #     pass

            if old_image_path:
                os.remove(old_image_path)

            form.save()

            return redirect('view profile')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
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


def user_library(request):
    profile = Profile.objects.get(pk=request.user.id)
    books = Book.objects.filter(user_id=request.user.id)

    context = {
        'user': profile,
        'books': books,
    }

    return render(request, 'accounts/user-library.html', context)
