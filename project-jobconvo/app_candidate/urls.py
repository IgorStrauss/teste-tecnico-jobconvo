from django.urls import path

from .service_jobs import (ApplicationCreateView, JobsListView,
                           ListJobsDetailView)
from .views import (CandidateCreateView, CandidateDeleteView,
                    CandidateListView, CandidateLoginView, CandidateLogoutView,
                    CandidateUpdateView, ExperienceCreateView,
                    ExperienceListView, ExperienceUpdateView,
                    HomeCandidateView)

app_name = 'app_candidate'


urlpatterns = [
    path("", HomeCandidateView.as_view(), name="home_candidate"),
    path("registrar-candidato/", CandidateCreateView.as_view(),
         name="create_candidate"),
    path("login-candidato/", CandidateLoginView.as_view(),
         name="login_candidate"),
    path("atualizar-candidato/<int:pk>/",
         CandidateUpdateView.as_view(), name="update_candidate"),
    path("listar-candidatos/", CandidateListView.as_view(),
         name="list_candidate"),
    path("cadastrar-experiencia/<int:candidate_id>/",
         ExperienceCreateView.as_view(), name="create_experience"),
    path("deletar-candidato/<int:pk>/",
         CandidateDeleteView.as_view(), name="delete_candidate"),
    path("logout-candidato/", CandidateLogoutView.as_view(),
         name="logout_candidate"),
    path("vaga-disponivel/<int:jobs_id>/",
         JobsListView.as_view(), name="list_jobs_candidate",),
    path("listar-experiencias/<int:candidate_id>/",
         ExperienceListView.as_view(), name="list_experience"),
    path("atualizar-experiencia/candidato/<int:candidate_id>/experiencia/<int:pk>/",
         ExperienceUpdateView.as_view(), name="update_experience"),
    path("vaga/<int:jobs_id>/", ListJobsDetailView.as_view(), name="list_job_id",),
    path("aplicar-vaga/candidato/<int:pk>/vaga/<int:jobs_id>/",
         ApplicationCreateView.as_view(), name="application_in_jobs")
]
