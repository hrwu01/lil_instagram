from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from insta.models import Post

# Create your views here.
class HelloWorld(TemplateView):
    template_name = 'dummy.html'

class PostsView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'