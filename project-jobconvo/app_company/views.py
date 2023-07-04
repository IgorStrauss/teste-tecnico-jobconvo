from typing import Any, Dict

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import CompanyForm, ContactCompanyForm, JobsForm, RequirementsForm
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
