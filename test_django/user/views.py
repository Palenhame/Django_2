from django.contrib.auth import logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from .models import Profile


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('main:main')
    else:
        form = UserRegisterForm()
    return render(request, 'form1.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('user:login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'form1.html'
    extra_context = {'title': 'djdj'}


# TODO ДОДЕЛАТЬ ПОКАЗАНИЕ СТАТЕЙ ПОЛЬЗОВАТЕЛЯ
# def account(request):
#     data = User.objects.filter(username=request.user).select_related('profile')
#     print(data)
#     print(data[0].title_set)
#     #     # return render(request, 'account.html')
#     return HttpResponse(data)
