from typing import Any, Dict

from app_company.models import Application, Jobs
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .forms import ApplicationCreateForm


class JobsListView(LoginRequiredMixin, DetailView):
    """Listar todas as vagas ativas para os candidatos logados"""
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


class ListJobsDetailView(LoginRequiredMixin, DetailView):
    """Listar vaga ativas por ID para os candidatos logados"""
    model = Jobs
    template_name = 'jobs/jobs_detail.html'
    context = 'jobs'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        if not self.request.user.is_authenticated:
            messages.warning(self.request, 'Você precisa estar logado!')
            return redirect(self.get_login_url())
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        jobs_id = self.kwargs.get('jobs_id')
        queryset = Jobs.objects.filter(is_active=True)
        return get_object_or_404(queryset, id=jobs_id)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['salary_range_choices'] = Jobs.salary_range
        return context


class ApplicationCreateView(LoginRequiredMixin, CreateView):
    """Gera correspondencia entre candidato_id e vaga_id"""
    model = Application
    form_class = ApplicationCreateForm
    template_name = 'jobs/application_create.html'
    success_url = reverse_lazy('app_candidate:home_candidate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['candidate_id'] = self.kwargs['pk']
        context['candidate'] = get_object_or_404(
            User, id=self.kwargs['pk'])
        context['job'] = get_object_or_404(Jobs, id=self.kwargs['jobs_id'])
        return context

    def form_valid(self, form):
        candidate = get_object_or_404(User, id=self.kwargs['pk'])
        job = get_object_or_404(Jobs, id=self.kwargs['jobs_id'])

        if Application.objects.filter(candidate=candidate, job=job).exists():
            messages.warning(
                self.request, 'Você já se candidatou a esta vaga!')
            return redirect('app_candidate:home_candidate')

        form.instance.candidate = candidate
        form.instance.job = job
        messages.success(
            self.request, f'Você se candidatou à vaga { job.title } de com sucesso!')
        return super().form_valid(form)
