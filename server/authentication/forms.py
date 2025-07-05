from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nombre de Usuario"
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput
    )

    remember = forms.BooleanField(
        required=False,
        label="Recordarme"
    )


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Nombre de Usuario",
    )

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):
    # image = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username',)
