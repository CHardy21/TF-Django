# apps/user/urls.py
from django.contrib.auth.views import LoginView, LogoutView
from .views import ProfileUpdateView, SignUpView, ProfileView, EditUserView
from django.urls import path

app_name = "user"  

urlpatterns = [
    path("register/", SignUpView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path('edit/', ProfileUpdateView.as_view(), name='edit_profile'),
  
]
