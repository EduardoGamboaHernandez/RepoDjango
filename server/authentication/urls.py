from django.urls import path, reverse_lazy
from .views import LoginView, LogoutView, SignUpView

urlpatterns = [
    path('login/', LoginView.as_view(success_url=reverse_lazy('inicio')), name="auth_login"),
    path('signup/', SignUpView.as_view(success_url=reverse_lazy('inicio')), name="auth_signup"),
    path('logout/', LogoutView.as_view(), name="auth_logout"),
]
