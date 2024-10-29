from django import forms
from .repository import create_repo

class CreateRepo(forms.Form):
    name = forms.CharField(label="Nombre del repositorio", max_length=20)
    description = forms.CharField(label="Descripcion", max_length=200, help_text="desc")

    def save(self):
        print("=="*20)
        print(self.cleaned_data["name"])
        create_repo(self.cleaned_data["name"], self.cleaned_data["description"])
from django import forms
# from django_widget_tweaks.forms import *

class MyForm(forms.Form):
    name = forms.CharField(
            max_length=30,
            label="Nombre del Repositorio",
            help_text="El nombre del repositorio será utilizado para identificarlo.",
            widget=forms.TextInput(attrs={'placeholder': 'Ingrese un nombre claro y conciso'})
        )
    description = forms.CharField(
            widget=forms.Textarea(attrs={'placeholder': 'Proporcione una breve descripción del repositorio'}),
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
            widget=forms.URLInput(attrs={'placeholder': 'https://github.com/tu-usuario/tu-repositorio.git'})
        )
    readme_md = forms.BooleanField(label="Crear un archivo README.md básico", required=False)