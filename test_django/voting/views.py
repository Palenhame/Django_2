from django.shortcuts import render, redirect
from .form import VotingForm
from .models import VotingModel


# Create your views here.
def voting(request, voting_id):
    votings = VotingModel.objects.all()
    if request.method == 'POST':
        print(request.POST)
        voting = votings.filter(pk=voting_id)
        voting.update({request.POST['exampleRadios']: 1})
    else:
        print('get')
    return render(request, 'voting.html', {'voting': votings})


def create_voting(request):
    votings = VotingModel.objects.all()
    if request.method == 'POST':
        form = VotingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:form')
    else:
        form = VotingForm()
    return render(request, 'create_voting.html', {'voting': votings, 'form': form})
