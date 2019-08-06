from django.urls import path

from authentication import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(),name = 'signup')
]