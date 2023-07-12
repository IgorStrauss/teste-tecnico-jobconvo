from typing import Any, Dict

from app_company.models import Jobs
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import CandidateForm, CandidateUpdateForm, ExperienceForm
from .models import Candidate, Experience


class HomeCandidateView(LoginRequiredMixin, ListView):
    template_name = 'home_candidate.html'
    model = Jobs
    queryset = Jobs.objects.filter(is_active=True).order_by('-created_at')
    context_object_name = 'jobs_list'
    login_url = reverse_lazy('app_candidate:login_candidate')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        if not self.request.user.is_authenticated:
            messages.warning(self.request, 'Você precisa estar logado!')
            return redirect(self.get_login_url())
        return super().dispatch(request, *args, **kwargs)


class CandidateCreateView(CreateView):
    model = Candidate
    form_class = CandidateForm
    template_name = 'create_candidate.html'
    success_url = reverse_lazy('app_candidate:list_candidate')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, 'Cadastro realizado com sucesso!')
        return super().form_valid(form)


class CandidateListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'list_candidates.html'
    queryset = User.objects.all()
    context_object_name = 'candidate_list'
    login_url = reverse_lazy('app_candidate:login_candidate')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if not self.request.user.is_authenticated:
            messages.warning(self.request, 'Você precisa estar logado!')
            return redirect(self.get_login_url())
        return super().dispatch(request, *args, **kwargs)


class CandidateUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CandidateUpdateForm
    template_name = 'update_candidate.html'
    success_url = reverse_lazy('app_candidate:home_candidate')
    login_url = reverse_lazy('app_candidate:login_candidate')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if not self.request.user.is_authenticated:
            messages.warning(self.request, 'Você precisa estar logado!')
            return redirect(self.get_login_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, 'Cadastro atualizado com sucesso!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['candidate_id'] = self.kwargs['pk']
        return context


class CandidateLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login_candidate.html'

    def get_success_url(self) -> str:
        messages.success(self.request, 'Login realizado com sucesso!')
        return reverse_lazy('app_candidate:home_candidate')


class CandidateLogoutView(LogoutView):
    success_url = reverse_lazy('app_candidate:home_candidate')

    def get_success_url(self) -> str:
        messages.success(self.request, 'Logout realizado com sucesso!')
        return reverse_lazy('home')


class CandidateDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'delete_candidate.html'
    success_url = reverse_lazy('app_candidate:list_candidate')
    login_url = reverse_lazy('app_candidate:login_candidate')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if not self.request.user.is_authenticated:
            messages.warning(self.request, 'Você precisa estar logado!')
            return redirect(self.get_login_url())
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self) -> str:
        messages.warning(self.request, 'Registro deletado com sucesso!')
        return reverse_lazy('app_candidate:list_candidate')


class ExperienceCreateView(CreateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'experience_create.html'
    success_url = reverse_lazy('app_candidate:home_candidate')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.kwargs['candidate_id']
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user_id = self.kwargs['candidate_id']
        messages.success(self.request, 'Requisito cadastrados com sucesso!')
        return super().form_valid(form)


class ExperienceListView(LoginRequiredMixin, ListView):
    model = Experience
    template_name = 'list_experience.html'
    context_object_name = 'experience_list'
    login_url = reverse_lazy('app_candidate:login_candidate')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if not self.request.user.is_authenticated:
            messages.warning(self.request, 'Você precisa estar logado!')
            return redirect(self.get_login_url())

        candidate_id = self.kwargs['candidate_id']
        if candidate_id != self.request.user.id:
            messages.warning(
                self.request, 'Acesso negado para consultar outros usuários!')
            return redirect('app_candidate:home_candidate')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self) -> QuerySet[Any]:
        candidate_id = self.kwargs['candidate_id']
        queryset = super().get_queryset()
        queryset = queryset.filter(user_id=candidate_id)
        return queryset


class ExperienceUpdateView(LoginRequiredMixin, UpdateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'update_experience.html'
    success_url = reverse_lazy('app_candidate:home_candidate')
    login_url = reverse_lazy('app_candidate:login_candidate')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if not self.request.user.is_authenticated:
            messages.warning(self.request, 'Você precisa estar logado!')
            return redirect(self.get_login_url())

        candidate_id = self.kwargs.get('candidate_id')
        if candidate_id != self.request.user.id:
            messages.warning(
                self.request, 'Acesso negado para consultar outros usuários!')
            return redirect('app_candidate:home_candidate')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        self.object = self.get_object()
        if self.object.user_id != self.kwargs['candidate_id']:
            messages.warning(
                self.request, 'Acesso negado para atualizar outras experiencias!')
            return redirect('app_candidate:home_candidate')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, 'Experiencia atualizada com sucesso!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.kwargs['candidate_id']
        return context
