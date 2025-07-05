from django.urls import path
from .views import LoginView, LogoutView, SignUpView

urlpatterns = [
    path('login/', LoginView.as_view(), name="auth_login"),
    path('signup/', SignUpView.as_view(), name="auth_signup"),
    path('logout/', LogoutView.as_view(), name="auth_logout"),
]
