from typing import Any, Dict

from app_company.models import Jobs
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView


class JobsListView(LoginRequiredMixin, DetailView):
    model = Jobs
    template_name = 'jobs/jobs_list_candidate.html'
    context_object_name = 'jobs_list'
    login_url = reverse_lazy('app_candidate:login_candidate')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        if not self.request.user.is_authenticated:
            messages.warning(self.request, 'Você precisa estar logado!')
            return redirect(self.get_login_url())
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        jobs_id = self.kwargs.get('jobs_id')
        queryset = Jobs.objects.filter(is_active=True)
        return get_object_or_404(queryset, id=jobs_id)
