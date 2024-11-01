import git
import os.path.join as path_join


class CreateRepo:
    def __init__(self, name: str, path_to_repos: str):
        self.path_to_repos = path_to_repos
        self.name_repo = name

        self._description = False
        self._remote = False

    def set_description(self, description: str):
        self._description = description

    def set_remote(self, name: str, url: str):
        self._remote = [name, url]

    def create(self):
        repo_path = path_join(self.path_to_repos, f"{self.name_repo}.git")

        self._repo = git.Repo.init(repo_path, bare=True, mkdir=True)

        if self._description:
            self._repo.description = self._description

        if self._remote:
            self._repo.create_remote(self._remote[0], self._remote[1])
