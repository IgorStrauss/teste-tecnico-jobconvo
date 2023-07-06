from typing import Any, Dict

from django.contrib import messages
from django.db.models import Q
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, UpdateView

from .forms import (CompanyForm, ContactCompanyForm, JobsForm, JobsUpdateForm,
                    RequirementsForm)
from .models import Company, ContactCompany, Jobs, Requirements


class HomeCompanyView(TemplateView):
    template_name = 'home_company.html'


class CompanyCreateView(CreateView):
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


class CompanyListView(ListView):
    model = Company
    template_name = 'company_list.html'
    queryset = Company.objects.all()
    context_object_name = 'company_list'


# class ListRegistrationCompany(CompanyListView):
#     model = Company
#     template_name = 'home_company.html'

#     def get_queryset(self) -> QuerySet[Any]:
#         queryset = super().get_queryset()
#         if termo := self.request.GET.get('termo'):
#             queryset = queryset.filter(Q(code__exact=termo))
#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if termo := self.request.GET.get('termo'):
#             company = self.get_queryset().first()
#             context["companies"] = [company] if company else []
#         else:
#             context["companies"] = []
#         return context


class JobsCreateView(CreateView):
    model = Jobs
    form_class = JobsForm
    template_name = 'jobs_create.html'
    success_url = reverse_lazy('app_company:home_company')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        company_id = self.kwargs['company_id']
        context['comp'] = get_object_or_404(Company, id=company_id)
        return context

    def form_valid(self, form):
        company_id = self.kwargs['company_id']
        form.instance.company_id = company_id
        messages.success(self.request, 'Vaga cadastrada com sucesso!')
        return super().form_valid(form)


class JobsListView(ListView):
    model = Jobs
    template_name = 'jobs_list.html'
    queryset = Jobs.objects.all()
    context_object_name = 'jobs_list'


class JobsUpdateView(UpdateView):
    model = Jobs
    form_class = JobsUpdateForm
    template_name = 'jobs_update.html'
    success_url = reverse_lazy('app_company:home_company')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, 'Vaga atualizada com sucesso!')
        return super().form_valid(form)


class RequirementsView(CreateView):
    model = Requirements
    form_class = RequirementsForm
    template_name = 'jobs_requirements.html'
    success_url = reverse_lazy('app_company:home_company')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, 'Requisito cadastrados com sucesso!')
        return super().form_valid(form)
