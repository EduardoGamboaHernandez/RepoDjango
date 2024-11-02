from django import forms
from .models import RepoModel


class RepoForm(forms.ModelForm):
    class Meta:
        model = RepoModel
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'Ingrese un nombre claro y conciso'}),
        }
        labels = {
            "name": "Nombre del Repositorio",
        }
        help_texts = {
            "name": "El nombre del repositorio será utilizado para identificarlo.",
        }

    description = forms.CharField(
        max_length=250,
        widget=forms.Textarea(
            attrs={'placeholder': 'Proporcione una breve descripción del repositorio'}),
        required=False,
        label="Descripción (opcional)",
        help_text="Describe el propósito y contenido del repositorio.",
    )

    remote = forms.CharField(
        max_length=100,
        label="URL del Remoto (Opcional)",
        required=False,
        help_text="Ingrese la URL del repositorio remoto para enlazarlo.",
        widget=forms.TextInput(
            attrs={'placeholder': 'https://github.com/tu-usuario/tu-repositorio.git'})
    )
