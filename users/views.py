from django.shortcuts import render

from django.views.generic import DetailView
from allmodels.models import InstaUser

class UserDetailView(DetailView):
    model = InstaUser
    template_name = 'user_detail.html'
