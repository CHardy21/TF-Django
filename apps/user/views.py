# apps/user/views.py
from django.contrib.auth import login
from .forms import EditProfileForm, SignUpForm, UserUpdateForm
from django.views.generic import FormView,TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpView(FormView):
    template_name = "registration/register.html"
    form_class = SignUpForm
    success_url = reverse_lazy("user:profile")  

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "user/profile.html"

class EditUserView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["first_name", "last_name", "email"]
    template_name = "user/edit_user.html"
    success_url = reverse_lazy("user:profile")

    def get_object(self):
        return self.request.user

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    #fields = ["avatar", "first_name", "last_name", "email"]
    form_class = EditProfileForm
    template_name = 'user/edit_profile.html'
    success_url = reverse_lazy('user:profile')  

    def get_object(self):
        return self.request.user
    
