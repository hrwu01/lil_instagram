from django.urls import path

from users import views

urlpatterns = [
    path('user/<int:pk>', views.UserDetailView.as_view(),name = 'user_detail'),
]