from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Kweet

class KweetForm(forms.ModelForm):
    class Meta:
        model = Kweet
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autocomplete': 'email', 'id': 'id_email'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'autocomplete': 'username', 'id': 'id_username'}),
            'password1': forms.PasswordInput(attrs={'autocomplete': 'new-password', 'id': 'id_password1'}),
            'password2': forms.PasswordInput(attrs={'autocomplete': 'new-password', 'id': 'id_password2'}),
        }