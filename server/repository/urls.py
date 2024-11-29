from django.urls import path
from .views import CreateRepoView, ShowRepoView, ShowListRepoView, ListCommitsView

urlpatterns = [
    path('crear/', CreateRepoView.as_view(), name="repo_create"),
    path('<str:username>/<str:repo>', ShowRepoView.as_view(), name="repo_show"),
    path('<str:username>/', ShowListRepoView.as_view(), name="repo_list"),
    path('commits/<str:username>/<str:repo>/', ListCommitsView.as_view(), name="repo_list_commits"),
]
