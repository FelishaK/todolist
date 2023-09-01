from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'complete']
        widgets = {'title':forms.TextInput(
            attrs = {'class':'form-control form-control-lg',
                     'placeholder':'What do you need to do today?'})}

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
