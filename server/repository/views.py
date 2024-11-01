from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CreateRepo

# Create your views here.

class CreateRepoView(generic.FormView):
    template_name = 'repository/create.html'
    form_class = CreateRepo
    success_url = reverse_lazy('repo_create')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
