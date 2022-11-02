from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a title to task'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a description to task'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
