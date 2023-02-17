from django import forms
from .models import NoteContent


class NoteForm(forms.ModelForm):
    class Meta:
        model = NoteContent
        fields = ('note',)
        widgets = {
            'note': forms.Textarea(attrs={'placeholder': 'Введите текст'}),
        }


class NoteSearchForm(forms.Form):
    query = forms.CharField(label='Search')