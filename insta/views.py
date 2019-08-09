from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from insta.models import Post
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class InstaRoot(TemplateView):
    template_name = 'dummy.html'

class PostListView(ListView):
    model = Post
    template_name = 'posts.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = '__all__'
    success_url = reverse_lazy('posts')
    login_url = 'login'

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = '__all__'
    success_url = reverse_lazy('posts')
    login_url = 'login'
    
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('posts')
    login_url = 'login'

