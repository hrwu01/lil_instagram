from django.urls import path

from insta import views

urlpatterns = [
    path('', views.InstaRoot.as_view(),name = 'insta_root'),
    path('posts/', views.PostListView.as_view(),name = 'posts'),
    path('posts/new', views.PostCreateView.as_view(),name = 'create_post'),
    path('posts/detail/<int:pk>', views.PostDetailView.as_view(),name = 'post_detail'),
    path('posts/update/<int:pk>', views.PostUpdateView.as_view(),name = 'update_post'),
    path('posts/delete/<int:pk>', views.PostDeleteView.as_view(),name = 'delete_post')
]