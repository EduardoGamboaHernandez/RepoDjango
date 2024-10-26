from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordChangeDoneView
from django.urls import path, reverse_lazy
from .views import index, SignUpView

urlpatterns = [
    path('login/', LoginView.as_view(template_name="user/login.html"), name="login_user"),
    path('change/', PasswordChangeView.as_view(template_name="user/pass-change.html", success_url=reverse_lazy('pass_change_done_user')), name="pass_change_user"),
    path('done/', PasswordChangeDoneView.as_view(template_name="user/pass-change-done.html", ), name="pass_change_done_user"),
    
    # implementar password_reset_confirm para recuperar la contraseña
    path('reset/', PasswordResetView.as_view(template_name="user/pass-change.html"), name="pass_reset_user"),

    path('logout/', LogoutView.as_view(), name="logout_user"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('', index, name='inicio')
]