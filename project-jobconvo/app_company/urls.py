from .views import home_company_view
from django.urls import path

app_name = 'app_company'


urlpatterns = [
    path("", home_company_view, name="home_company"),
]
