from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


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


def logout(request):
    logout(request)
    redirect('login')


def login(request):
    pass

