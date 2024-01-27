from django import forms
from .models import NewsModel


class TestForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = ['title', 'img', 'type', 'text_news']
