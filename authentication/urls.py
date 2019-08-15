from django.urls import path

from authentication import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(),name = 'signup'),
    path('edit/<int:pk>',views.EditProfile.as_view(),name = 'edit_profile'),
]