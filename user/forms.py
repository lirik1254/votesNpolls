from django import forms
from .models import Poll, Choice


class PollForm(forms.ModelForm):
    # title = forms.CharField(max_length=255)
    # description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Poll
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название голосования'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание голосования'}),
        }

class ChoiceForm(forms.ModelForm):
    # text = forms.CharField(max_length=255)

    class Meta:
        model = Choice
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите вариант ответа'}),
        }