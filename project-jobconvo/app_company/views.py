from typing import Any, Dict

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, TemplateView, UpdateView

from .forms import (CompanyForm, CompanyOwnerLoginForm,
                    CompanyOwnerRegisterForm, ContactCompanyForm, JobsForm,
                    JobsUpdateForm, RequirementsForm)
from .models import Application, Company, Jobs, Requirements


class HomeCompanyView(TemplateView):
    template_name = 'home_company_pre.html'


class CompanyOwnerRegisterView(CreateView):
    model = User
    form_class = CompanyOwnerRegisterForm
    template_name = 'company_owner_register.html'
    success_url = reverse_lazy('app_company:login_company_owner')


class CompanyOwnerLoginView(LoginView):
    """Login para companhia"""
    form_class = AuthenticationForm
    template_name = 'login_company_owner.html'

    def get_success_url(self) -> str:
        messages.success(self.request, 'Login realizado com sucesso!')
        return reverse_lazy('app_company:home_company')


class CompanyOwnerLogoutView(LoginRequiredMixin, LogoutView):
    """Logout para companhia"""
    success_url = reverse_lazy('app_company:login_company_owner')

    def get_success_url(self) -> str:
        messages.success(self.request, 'Desconectado com sucesso!')
        return reverse_lazy('app_company:login_company_owner')


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company_create.html'
    success_url = reverse_lazy('app_company:home_company')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['contact_form'] = ContactCompanyForm(self.request.POST)
        else:
            context['contact_form'] = ContactCompanyForm()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        contact_form = context['contact_form']
        if contact_form.is_valid():
            return self._context_form_company_contact(form, contact_form)
        return self.render_to_response(self.get_context_data(form=form))

    def _context_form_company_contact(self, form, contact_form):
        self.object = form.save()
        contact = contact_form.save(commit=False)
        contact.company = self.object
        contact.save()
        messages.success(self.request, 'Empresa cadastrada com sucesso!')
        return HttpResponseRedirect(self.get_success_url())


class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'company_list.html'
    queryset = Company.objects.all()
    context_object_name = 'company_list'


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company_update.html'
    success_url = reverse_lazy('app_company:home_company')

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
        context['company_id'] = self.kwargs['pk']
        return context


class JobsCreateView(LoginRequiredMixin, CreateView):
    model = Jobs
    form_class = JobsForm
    template_name = 'jobs_create.html'
    success_url = reverse_lazy('app_company:home_company')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        company_id = self.kwargs['company_id']
        kwargs['company_id'] = company_id
        return kwargs

    def form_valid(self, form):
        company_id = self.kwargs['company_id']
        company = get_object_or_404(Company, id=company_id)
        form.instance.company = company
        messages.success(self.request, 'Vaga cadastrada com sucesso!')
        return super().form_valid(form)


class JobsActiveListView(LoginRequiredMixin, ListView):
    model = Jobs
    template_name = 'jobs_list.html'
    queryset = Jobs.objects.filter(is_active=True).order_by('-created_at')
    context_object_name = 'jobs_list'


class JobsInactiveListView(LoginRequiredMixin, ListView):
    model = Jobs
    template_name = 'jobs_list_inactive.html'
    queryset = Jobs.objects.filter(is_active=False)
    context_object_name = 'jobs_list'


class JobsUpdateView(LoginRequiredMixin, UpdateView):
    model = Jobs
    form_class = JobsUpdateForm
    template_name = 'jobs_update.html'
    success_url = reverse_lazy('app_company:home_company')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['requirements_list'] = Requirements.objects.all()
        context['jobs'] = self.object
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, 'Vaga atualizada com sucesso!')
        return super().form_valid(form)


class RequirementsView(LoginRequiredMixin, CreateView):
    model = Requirements
    form_class = RequirementsForm
    template_name = 'jobs_requirements.html'
    success_url = reverse_lazy('app_company:home_company')
    context_object_name = 'requirements_list'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['requirements_list'] = Requirements.objects.all()
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, 'Requisito cadastrados com sucesso!')
        return super().form_valid(form)
