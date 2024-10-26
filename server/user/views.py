from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login_user")
    template_name = "users/signup.html"


@login_required(login_url="login_user")
def index(request):
    return render(request, "user/index.html")
