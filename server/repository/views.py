from django.urls import reverse_lazy
from django.views import generic
from .forms import RepoForm
from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
from git.exc import NoSuchPathError
from .models import RepoModel
from django.contrib.auth.models import User
import os

from .RepoLib.repo import Repo
from .RepoLib.commit import Commit
from .RepoLib.files import Files


REPOS_DIR = getattr(settings, "REPOS_DIR", None)


def home(request):
    return redirect('repo_list', username=request.user.username)


class CreateRepoView(generic.FormView):
    template_name = 'repository/create-repo.html'
    form_class = RepoForm
    success_url = reverse_lazy('repo_create')

    def form_valid(self, model):
        instance = model.save(commit=False)
        instance.user = self.request.user
        instance.remote = self.request.POST.get('remote')
        instance.save()
        return super().form_valid(model)


class ShowRepoView(generic.View):
    template_name = "repository/show-repo.html"

    def get(self, request, username, reponame):
        branch_query = request.GET.getlist('branch')
        path = os.path.join(REPOS_DIR, username)
        context = {
            "username": username,
            "repo": reponame
        }

        try:
            repo = Repo(reponame, path)
            commit = Commit(reponame, path)
            files = Files(reponame, path)

            info = repo.get_info("main")

            if branch_query:
                info["active_branch"] = branch_query[0]

            last_commit = commit.get_last_commit(info["active_branch"])
            tree = files.get_tree(last_commit["hash"])
            tags = tags = repo.get_tags()
            context["info"] = info
            context["last_commit"] = last_commit
            context["tree"] = tree
            context["tags"] = tags
        except NoSuchPathError:
            print("poner un 404: repositorio no encontrado")

        return render(request, self.template_name, context)


class ShowListRepoView(generic.ListView):
    template_name = "repository/list-repo.html"
    model = RepoModel
    paginate_by = 20

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs["username"])
        return self.model.objects.filter(user=user)


class ListCommitsView(generic.View):
    template_name = "repository/list-commits.html"

    def get(self, request, username, repo):
        path = os.path.join(REPOS_DIR, username)
        context = {}

        try:
            commit = Commit(repo, path)
            context['commits_list'] = commit.get_commit_list()
        except NoSuchPathError:
            print("poner un 404: repositorio no encontrado")

        return render(request, self.template_name, context)


class ShowFileView(generic.View):
    template_name = "repository/show-file.html"

    def get(self, request, username, repo, file):
        path = os.path.join(REPOS_DIR, username)
        context = {}

        try:
            files = Files(repo, path)
            context['file'] = files.get_file_content("4d05683", file)
        except NoSuchPathError:
            print("poner un 404: archivo no encontrado")

        return render(request, self.template_name, context)
