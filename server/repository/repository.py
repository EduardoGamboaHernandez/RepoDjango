from django.conf import settings
import git
import os


REPOS_DIR = getattr(settings, "REPOS_DIR", None)
def create_repo(name, description):
    repo_path = f"{REPOS_DIR}/{name}.git"
    repo = git.Repo.init(repo_path, bare=True, mkdir=True)
    repo.description = description
    if(repo):
        print(f"Nuevo repositorio bare creado en: {repo_path}")


if __name__ == "__main__":
    print(REPOS_DIR)