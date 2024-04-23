from django import forms
from .models import Orderer, Executor, Experience


class OrdererForm(forms.ModelForm):
    class Meta:
        model = Orderer
        exclude = ['user']


class ExecutorForm(forms.ModelForm):
    class Meta:
        model = Executor
        exclude = ['user']


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ['user']
