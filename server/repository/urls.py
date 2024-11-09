from django.urls import path
from .views import CreateRepoView, ShowRepoView

urlpatterns = [
    path('crear/', CreateRepoView.as_view(), name="repo_create"),
    path('ver/<str:username>/<str:repo>', ShowRepoView.as_view(), name="repo_show"),
]
