from django.urls import path
from .views import CreateRepoView, ShowRepoView, ShowListRepoView

urlpatterns = [
    path('crear/', CreateRepoView.as_view(), name="repo_create"),
    path('<str:username>/<str:repo>', ShowRepoView.as_view(), name="repo_show"),
    path('<str:username>/', ShowListRepoView.as_view(), name="repo_list"),
]
