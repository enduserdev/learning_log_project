from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        # Specify the model class
        model = Topic
        # Specify which fields to use
        fields = ['text']
        labels = {'text': ' '}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ' '}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
