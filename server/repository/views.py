from django.urls import reverse_lazy
from django.views import generic
from .forms import RepoForm


# Create your views here.
class CreateRepoView(generic.FormView):
    template_name = 'repository/create.html'
    form_class = RepoForm
    success_url = reverse_lazy('repo_create')

    def form_valid(self, model):
        instance = model.save(commit=False)
        instance.user = self.request.user
        instance.description = self.request.POST.get('description')
        instance.remote = self.request.POST.get('remote')
        instance.save()
        return super().form_valid(model)
