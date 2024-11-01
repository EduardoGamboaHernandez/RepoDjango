from django.conf import settings
from django import forms
from .repository import CreateRepo
import os


REPOS_DIR = getattr(settings, "REPOS_DIR", None)


class CreateRepo(forms.Form):
    name = forms.CharField(
        max_length=30,
        label="Nombre del Repositorio",
        help_text="El nombre del repositorio será utilizado para identificarlo.",
        widget=forms.TextInput(
            attrs={'placeholder': 'Ingrese un nombre claro y conciso'})
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Proporcione una breve descripción del repositorio'}),
        max_length=100,
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
    readme_md = forms.BooleanField(
        label="Crear un archivo README.md básico", required=False)

    def save(self):
        print("=="*20)
        repos_dir = path = os.path.join(REPOS_DIR, )
        repo = CreateRepo(self.cleaned_data["name"], REPOS_DIR)
        repo.set_description(self.cleaned_data["description"])
        repo.set_remote("origin", self.cleaned_data["remote"])
        repo.create()
