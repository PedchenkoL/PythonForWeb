# from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django import forms

class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()