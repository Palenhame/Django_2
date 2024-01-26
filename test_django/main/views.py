from django.shortcuts import render
from .models import Test
from .form import TestForm


# Create your views here.

def main(request):
    if request.method == 'POST':
        data = Test.objects.values_list('pk')
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = TestForm()
        data = None
    return render(request, 'index.html',
                  {'form': form, 'data': data})


def other(request, page):
    data = Test.objects.get(pk=page)
    return render(request, 'other.html', {'data': data})
