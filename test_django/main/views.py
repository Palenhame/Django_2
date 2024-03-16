from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from .models import NewsModel, CommentModel
from .form import TestForm, CommentForm


# Create your views here.

def main(request):
    return render(request, 'main.html')


def other(request, page):
    data = get_object_or_404(NewsModel, pk=page)
    try:
        data_comment = CommentModel.objects.all().filter(article=data)
    except:
        data_comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        print('all good')
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.article = data
            print('comment')
            comment.save()
            form = CommentForm()
            return render(request, 'other.html', {'data': data, 'data_comment': data_comment, 'form': form})
    else:
        form = CommentForm()
        print(data_comment)
    return render(request, 'other.html', {'data': data, 'data_comment': data_comment, 'form': form})


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


@login_required
def voting(request):
    return HttpResponse('All good')
