from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import NewsModel, CommentModel
from .form import TestForm


# Create your views here.

def main(request):
    return render(request, 'main.html')


def other(request, page):
    data = NewsModel.objects.get(pk=page)
    try:
        data_comment = CommentModel.objects.get(pk=page)
    except:
        data_comment = None
    return render(request, 'other.html', {'data': data, 'data_comment': data_comment})


@login_required
def form(request):
    global data
    if request.method == 'POST':
        form = TestForm(request.POST, request.FILES)
        print('all good')
        if form.is_valid():
            print(request.user)
            print(type(request.user))
            data = form.save(commit=False)
            data.author = request.user
            data = form.save()
            print('all good')
            return redirect('main:other', page=data.pk)

    else:
        form = TestForm()
        data = None
    return render(request, 'form.html',
                  {'form': form, 'data': data})


def news(request):
    data = NewsModel.objects.all()
    return render(request, 'news.html', {'data': data})
