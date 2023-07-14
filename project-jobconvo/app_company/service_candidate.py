from typing import Any, Dict

from app_candidate.models import Candidate, Experience
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Application, Jobs


class ApplicationCompanyListView(ListView):
    """Lista todas as vagas em que há candidatos inscritos, informando a quantidade de candidatos por vaga."""
    model = Application
    template_name = 'home_company.html'
    context_object_name = 'application_company_list'
    queryset = Application.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job_ids = context['application_company_list'].values_list(
            'job_id', flat=True).distinct()
        jobs = Jobs.objects.filter(id__in=job_ids)
        job_candidates = Application.objects.filter(job_id__in=job_ids).values(
            'job_id').annotate(num_candidates=Count('job_id'))
        job_candidates_dict = {
            job['job_id']: job['num_candidates'] for job in job_candidates}
        for job in jobs:
            job.num_candidates = job_candidates_dict.get(job.id, 0)
        context['jobs'] = jobs
        return context


class ApplicationCompanyListJobView(ListView):
    """Listar vaga por id com quantidade de candidatos, renderizando lista de candidatos.   """
    model = Application
    template_name = 'job_filter.html'
    context_object_name = 'application_company_list'
    queryset = Application.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job = get_object_or_404(Jobs, pk=self.kwargs['pk'])
        context['job'] = job
        context['num_candidates'] = Application.objects.filter(job=job).count()

        # Filtrar inscrições relacionadas ao job_id selecionado
        job_ids = [job.id]
        candidate_ids = Application.objects.filter(
            job_id__in=job_ids).values_list('candidate_id', flat=True).distinct()
        context['candidates'] = User.objects.filter(id__in=candidate_ids)

        return context


class CandidateDetailView(DetailView):
    model = User
    template_name = 'candidate_detail.html'
    context_object_name = 'candidate'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        candidate = self.get_object()
        experiences = Experience.objects.filter(user=candidate)
        context['experiences'] = experiences
        return context
