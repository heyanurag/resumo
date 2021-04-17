from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import register, account
from . import views


urlpatterns = [
    path('resume/', views.resume, name="resume"),
    path('create/', views.create, name="create"),
    path('create/education/', views.EducationCreateView.as_view(), name="education-form"),
    path('create/work/', views.WorkExperienceCreateView.as_view(), name="workexp-form"),
    path('create/skills/', views.SkillsCreateView.as_view(), name="skills-form"),
    path('create/interest/', views.InterestCreateView.as_view(), name="interest-form"),
    path('register/', register, name='register'),
    path('account/', account, name='account'),
    path('sign_in/', auth_views.LoginView.as_view(template_name='users/sign_in.html'), name='sign-in'),
    path('log_out/', auth_views.LogoutView.as_view(template_name='users/log_out.html'), name='sign-out'),
    path('about/', views.about, name="about"),
    path('', views.home, name="home")
]