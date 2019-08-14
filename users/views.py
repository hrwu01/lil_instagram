from django.shortcuts import render

from django.views.generic import DetailView
from authentication.models import InstaUser

class UserDetailView(DetailView):
    model = InstaUser
    template_name = 'user_detail.html'
