from django.shortcuts import render, redirect
from .models import NewsModel
from .form import TestForm


# Create your views here.

def main(request):
    return render(request, 'main.html')


def other(request, page):
    data = NewsModel.objects.get(pk=page)
    return render(request, 'other.html', {'data': data})


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
