from django.db import models
from django_hashids import HashidsField
from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch import receiver
import shutil
import os

from .RepoLib.bare import Bare

REPOS_DIR = getattr(settings, "REPOS_DIR", None)


class RepoModel(models.Model):
    """
    Modelo de la tabla que almacena información de los repositorios
    """
    hashid = HashidsField(real_field_name="id", min_length=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=600)
    created = models.DateTimeField(auto_now_add=True)
    remote = None

    def __str__(self):
        return self.user.username + "/" + self.name

    def save(self, *args, **kwargs):
        path = os.path.join(REPOS_DIR, self.user.username)
        # Crear el repositorio
        repo = Bare(self.name, path)
        repo.create(self.description, self.remote)

        return super().save(*args, **kwargs)


@receiver(models.signals.post_delete, sender=RepoModel)
def delete_repo_hook(sender, instance, using, **kwargs):
    """
    función que funciona como gancho al borrar un
    elemento de la base de datos también borrar el archivo .git
    """
    path = os.path.join(REPOS_DIR, instance.user.username, f"{instance.name}.git")
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        print("repositorio borrado")
