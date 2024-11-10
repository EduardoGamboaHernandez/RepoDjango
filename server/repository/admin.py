from django.contrib import admin
from .models import RepoModel


# Register your models here.
class RepoAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ["hashid", "user", "name", "description", "created"]


admin.site.register(RepoModel, RepoAdmin)
