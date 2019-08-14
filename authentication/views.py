from django.shortcuts import render
from authentication.forms import CustomUserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy

# Create your views here.
class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
