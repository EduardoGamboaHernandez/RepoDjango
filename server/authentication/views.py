from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import FormView
from .forms import CustomUserLoginForm, CustomUserCreationForm
from django.shortcuts import redirect
from django.utils import timezone
from .models import CustomUser
from django.conf import settings


class LoginView(FormView):
    template_name = "authentication/login.html"
    form_class = CustomUserLoginForm
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        remember = form.cleaned_data['remember']

        if remember == "on":
            self.request.session.set_expiry(604800)
        else:
            self.request.session.set_expiry(0)

        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            user.last_login = timezone.now

        return super().form_valid(form)


class SignUpView(FormView):
    template_name = "authentication/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        print(form.cleaned_data)

        password = None
        if password1 == password2:
            password = password1

        user = CustomUser.objects.create_user(username, password, first_name, last_name)

        if user is not None:
            login(self.request, user)
            user.last_login = timezone.now

        return super().form_valid(form)


class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect(reverse_lazy('auth_login'))
