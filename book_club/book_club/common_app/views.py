from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import View, TemplateView


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

# UserModel = get_user_model()
# def home(request):
#
#     users = UserModel.objects.all()
#
#     # context = {
#     #     'users': users
#     # }
#     return render(request, 'home.html')


# def about(request):
#     return render(request, 'about.html')

class AboutPageView(TemplateView):
    template_name = 'about.html'

