from django import forms
from .models import NewsModel, CommentModel


class TestForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = ['title', 'img', 'type', 'text_news']


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['text']
