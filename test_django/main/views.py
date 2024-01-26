from django.shortcuts import render
from .form import TestForm


# Create your views here.

def main(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = TestForm()
    return render(request, 'index.html', {'form': form})
