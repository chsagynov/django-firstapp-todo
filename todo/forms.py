from django import forms
from django.forms import ModelForm
from .models import Card, Task

class AddCardForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddCardForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Card
        exclude = []

class AddTaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddTaskForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Task
        exclude = []