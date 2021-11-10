from .models import Task, Person
from django import forms
from django.contrib.auth.forms import UserCreationForm


class PersonRegisterForm(UserCreationForm):

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'username', 'email', 'gender']
        exclude = ('last_login', 'is_superuser', 'is_active', 'groups', 'user_permissions', 'is_staff', 'date_joined')


class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ('is_complete', 'start_date', 'completed_date', 'owner')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
