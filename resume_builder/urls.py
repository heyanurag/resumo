from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from users.views import register, account, profile
from . import views


urlpatterns = [
    path('resume/', login_required(views.resume), name="resume"),
    path('create/', login_required(views.create), name="create"),
    path('create/education/', login_required(views.EducationCreateView.as_view()), name="education-form"),
    path('create/work/', login_required(views.WorkExperienceCreateView.as_view()), name="workexp-form"),
    path('create/skills/', login_required(views.SkillsCreateView.as_view()), name="skills-form"),
    path('create/interest/', login_required(views.InterestCreateView.as_view()), name="interest-form"),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('account/', login_required(account), name='account'),
    path('sign_in/', auth_views.LoginView.as_view(template_name='users/sign_in.html'), name='sign-in'),
    path('log_out/', auth_views.LogoutView.as_view(template_name='users/log_out.html'), name='sign-out'),
    path('about/', views.about, name="about"),
    path('', views.home, name="home")
]