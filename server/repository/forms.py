from django import forms
from .repository import create_repo

class CreateRepo(forms.Form):
    name = forms.CharField(label="Nombre del repositorio", max_length=20)
    description = forms.CharField(label="Descripcion", max_length=200, help_text="desc")

    def save(self):
        print("=="*20)
        print(self.cleaned_data["name"])
        create_repo(self.cleaned_data["name"], self.cleaned_data["description"])
