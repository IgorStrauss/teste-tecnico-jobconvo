from django.urls import path

from .views import (CompanyCreateView, CompanyListView, HomeCompanyView,
                    JobsCreateView, JobsListView, JobsUpdateView,
                    RequirementsView)

app_name = 'app_company'


urlpatterns = [
    path("", HomeCompanyView.as_view(), name="home_company"),
    path("register-company/", CompanyCreateView.as_view(),
         name="company_create"),
    path("register-jobs/<int:company_id>/",
         JobsCreateView.as_view(), name="jobs_create"),
    path("register-requirements/", RequirementsView.as_view(),
         name="requirements"),
    path("list-company/", CompanyListView.as_view(), name="list_company"),
    path("list-jobs/", JobsListView.as_view(), name="list_jobs"),
    path("update-jobs/<int:pk>/",
         JobsUpdateView.as_view(), name="update_jobs"),
]
