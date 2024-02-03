from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import NewsModel
from .form import TestForm


# Create your views here.

def main(request):
    return render(request, 'main.html')


def other(request, page):
    data = NewsModel.objects.get(pk=page)
    return render(request, 'other.html', {'data': data})


@login_required
def form(request):
    global data
    if request.method == 'POST':
        form = TestForm(request.POST, request.FILES)
        print('all good')
        if form.is_valid():
            print('all good')
            data = form.save()
            return redirect('main:other', page=data.pk)

    else:
        form = TestForm()
        data = None
    return render(request, 'form.html',
                  {'form': form, 'data': data})


def news(request):
    data = NewsModel.objects.all()
    print(data)
    return render(request, 'news.html', {'data': data})
