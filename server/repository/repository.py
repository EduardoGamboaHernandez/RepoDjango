import git
import os


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
        repo_path = os.path.join(self.path_to_repos, f"{self.name_repo}.git")

        self._repo = git.Repo.init(repo_path, bare=True, mkdir=True)

        if self._description:
            self._repo.description = self._description

        if self._remote:
            self._repo.create_remote(self._remote[0], self._remote[1])

        self._repo.index.commit("init: initial commit")


class GetRepoBranch:
    def __init__(self, name: str, path_to_repos: str):
        self.path_to_repos = path_to_repos
        self.name_repo = name
        repo_path = os.path.join(self.path_to_repos, f"{self.name_repo}.git")
        self._repo = git.Repo(repo_path)
        self.repo_dict = {
            "name": self.name_repo
        }

    def get_info(self, branch):
        if self._repo.bare:
            self.repo_dict["description"] = self._repo.description
            self.repo_dict["brranches"] = [branch.name for branch in self._repo.branches]
            self.repo_dict["active_branch"] = self._repo.active_branch.name
        return self.repo_dict

    def get_last_commit(self, branch='HEAD'):
        commit = list(self._repo.iter_commits(branch, max_count=1))[0]
        commit_dict = {
            "hash": commit.hexsha,
            "message": commit.message,
            "autor": commit.author.name,
            "date": commit.committed_datetime
        }
        return commit_dict

    def get_tree(self, commit_hash):
        commit = self._repo.commit(commit_hash)
        tree = []
        for tree_entry in commit.tree.traverse():
            tree.append({
                "name": tree_entry.path,
                "type": tree_entry.type,
                "size": tree_entry.size,
                # "sizex": tree_entry.mime_type,
            })
        return tree

    def get_tags(self):
        return [tag.name for tag in self._repo.tags]
