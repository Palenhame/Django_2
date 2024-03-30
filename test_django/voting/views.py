from django.shortcuts import render, redirect
from .form import VotingForm
from voting.models import VotingModel


# Create your views here.
def voting(request):
    votings = VotingModel.objects.all()
    if request.method == 'POST':
        form = VotingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:form')
    else:
        form = VotingForm()
    return render(request, 'voting.html', {'voting': votings, 'form': form})
