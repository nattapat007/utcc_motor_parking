from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from accounts.models import CustomUser


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ProfilePageView(generic.UpdateView):
    model = CustomUser
    fields = ["first_name"]
    success_url = reverse_lazy("home")
    template_name = "profile.html"
