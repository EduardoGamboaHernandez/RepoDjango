from django import forms
from .models import RepoModel


class RepoForm(forms.ModelForm):
    class Meta:
        model = RepoModel
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'Ingrese un nombre claro y conciso'}),
            "description": forms.Textarea(attrs={'placeholder': 'Proporcione una breve descripción del repositorio'}),
        }
        labels = {
            "name": "Nombre del Repositorio",
            "description": "Descripción (opcional)",
        }
        help_texts = {
            "name": "El nombre del repositorio será utilizado para identificarlo.",
            "description": "Describe el propósito y contenido del repositorio.",
        }

    remote = forms.CharField(
        max_length=100,
        label="URL del Remoto (Opcional)",
        required=False,
        help_text="Ingrese la URL del repositorio remoto para enlazarlo.",
        widget=forms.TextInput(
            attrs={'placeholder': 'https://github.com/tu-usuario/tu-repositorio.git'})
    )
