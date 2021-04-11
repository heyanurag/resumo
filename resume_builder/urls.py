from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import register
from . import views


urlpatterns = [
    path('create/', views.create, name="create"),
    path('register/', register, name='register'),
    path('sign_in/', auth_views.LoginView.as_view(template_name='users/sign_in.html'), name='sign-in'),
    path('log_out/', auth_views.LogoutView.as_view(template_name='users/log_out.html'), name='sign-out'),
    path('about/', views.about, name="about"),
    path('', views.home, name="home")
]