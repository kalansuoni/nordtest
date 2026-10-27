from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """Form for creating a topic."""

    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """Form for creating an entry."""

    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80}),
        }