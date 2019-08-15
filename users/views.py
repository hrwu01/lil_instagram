from django.shortcuts import render
from django.http import request
from django.views.generic import DetailView,TemplateView
from allmodels.models import InstaUser


class UserDetailView(DetailView):
    model = InstaUser
    template_name = 'user_detail.html'

