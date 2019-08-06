from authentication.models import InstaUser
from django import forms 
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = InstaUser
        fields = ('username', 'email', 'profile_pic')
        
