from django.urls import path
from .views import CreateRepoView

urlpatterns = [
    path('crear/', CreateRepoView.as_view(), name="repo_create"),
]
