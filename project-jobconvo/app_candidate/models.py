from django.contrib.auth.models import User
from django.db import models


class Candidate(models.Model):
    """Vinculada ao model User para criação do objeto candidato"""
    ...


class Experience(models.Model):
    """Cadastro de experiencia para candidato_id"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
