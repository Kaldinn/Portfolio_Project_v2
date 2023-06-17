from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 


class BudgetForm(forms.ModelForm):
    type = forms.ChoiceField(choices=Budget.TYPE_CHOICES)

    class Meta:
        model = Budget
        fields = ['title', 'type', 'tax', 'price']