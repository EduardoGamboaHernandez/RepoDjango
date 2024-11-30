from django.urls import path
from .views import CreateRepoView, ShowRepoView, ShowListRepoView, ListCommitsView, home

urlpatterns = [
    path('', home, name="repo_to_home"),
    path('crear/', CreateRepoView.as_view(), name="repo_create"),
    path('<str:username>/<str:repo>', ShowRepoView.as_view(), name="repo_show"),
    path(r'<username>/$', ShowListRepoView.as_view(), name="repo_list"),
    path('commits/<str:username>/<str:repo>/', ListCommitsView.as_view(), name="repo_list_commits"),
]
