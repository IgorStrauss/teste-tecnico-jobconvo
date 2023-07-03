from .views import home_candidate_view
from django.urls import path

app_name = 'app_candidate'


urlpatterns = [
    path("", home_candidate_view, name="home_candidate"),
]
