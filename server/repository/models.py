from django.db import models
from django_hashids import HashidsField
from django.contrib.auth.models import User
from django.conf import settings
from .repository import CreateRepo
import os


REPOS_DIR = getattr(settings, "REPOS_DIR", None)


# Create your models here.
class RepoModel(models.Model):
    hashid = HashidsField(real_field_name="id", min_length=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username + "/" + self.name

    def save(self, *args, **kwargs):
        path = os.path.join(REPOS_DIR, self.user.username)
        repo = CreateRepo(self.name, path)
        repo.set_description(self.description)
        repo.set_remote("origin", self.remote)
        repo.create()

        return super().save(*args, **kwargs)
