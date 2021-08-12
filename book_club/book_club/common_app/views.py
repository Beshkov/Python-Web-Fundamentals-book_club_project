from django.contrib.auth import get_user_model
from django.shortcuts import render



# def home(request):
#     return render(request, 'home.html')


UserModel = get_user_model()
def home(request):

    users = UserModel.objects.all()

    context = {
        'users': users
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')



