from django.urls import path

from .views import CompanyCreateView, HomeCompanyView

app_name = 'app_company'


urlpatterns = [
    path("", HomeCompanyView.as_view(), name="home_company"),
    path("register-company/", CompanyCreateView.as_view(),
         name="company_create"),
]
