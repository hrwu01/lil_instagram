from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from allmodels.models import Post,UserConnection,InstaUser
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class InstaRoot(TemplateView):
    template_name = 'dummy.html'

class PostListView(ListView):
    model = Post
    template_name = 'posts.html'

    # def get_queryset(self):
    #     if not self.request.user.is_authenticated:
    #         return None
    #     current_user = self.request.user
    #     following = set()
    #     following.add(current_user)
    #     for conn in UserConnection.objects.filter(creator=current_user).select_related('following'):
    #         following.add(conn.following)
    #     return Post.objects.filter(author__in=following)

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'post_detail.html'
    login_url = 'login'

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

