from django import forms
from .models import VotingModel


class VotingForm(forms.ModelForm):
    class Meta:
        model = VotingModel
        fields = ['text', 'value1', 'value2', 'value3', 'value4']


class VotingModelForm(forms.ModelForm):
    class Meta:
        model = VotingModel
        fields = ['text', 'value1', 'value2', 'value3', 'value4']
