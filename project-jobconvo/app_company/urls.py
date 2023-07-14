from django.urls import path

from .service_candidate import (ApplicationCompanyListJobView,
                                ApplicationCompanyListView,
                                CandidateDetailView)
from .views import (CompanyCreateView, CompanyListView, CompanyOwnerLoginView,
                    CompanyOwnerLogoutView, CompanyOwnerRegisterView,
                    CompanyUpdateView, HomeCompanyView, JobsActiveListView,
                    JobsCreateView, JobsInactiveListView, JobsUpdateView,
                    RequirementsView)

app_name = 'app_company'


urlpatterns = [
    path('register-owner-company-cnpj/',
         CompanyOwnerRegisterView.as_view(), name='register_owner_company'),
    path('login-company-rzn5236orq-k99mibehr9/',
         CompanyOwnerLoginView.as_view(), name='login_company_owner'),
    path('logout-company-orq-k99-mibehr9/',
         CompanyOwnerLogoutView.as_view(), name='logout_company_owner'),
    path("17arcyiekk/marques/96a014o8n8/igor/2023/",
         HomeCompanyView.as_view(), name="home_company133"),
    path("register-company/", CompanyCreateView.as_view(),
         name="company_create"),
    path("register-jobs/<int:company_id>/",
         JobsCreateView.as_view(), name="jobs_create"),
    path("company-update/<int:pk>/",
         CompanyUpdateView.as_view(), name="company_update"),
    path("register-requirements/", RequirementsView.as_view(),
         name="requirements"),
    path("list-company/", CompanyListView.as_view(), name="list_company"),
    path("list-jobs-active/", JobsActiveListView.as_view(),
         name="list_jobs_active"),
    path("update-jobs/<int:pk>/",
         JobsUpdateView.as_view(), name="update_jobs"),
    path("list-jobs-inactive/", JobsInactiveListView.as_view(),
         name="list_jobs_inactive"),
    #     path("selective-jobs/", ApplicationListView.as_view(),
    #          name="selective_jobs"),
    path("list-jobs-company/", ApplicationCompanyListView.as_view(),
         name="home_company"),
    path("list-jobs-company/<int:pk>/",
         ApplicationCompanyListJobView.as_view(),
         name="list_filter_job_company"),
    path("candidate-detail/<int:pk>/",
         CandidateDetailView.as_view(), name="candidate_detail"),
]
