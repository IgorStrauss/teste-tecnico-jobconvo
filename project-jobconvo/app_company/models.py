from datetime import datetime

from django.db import models

from .service import SALARY_CHOICES


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    @property
    def format_name(self):
        return f"{self.name}".capitalize()


class ContactCompany(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.DO_NOTHING, null=False)
    manager = models.CharField(
        max_length=45, null=False, verbose_name='Nome do responsável')
    email = models.EmailField(unique=True, null=False, verbose_name='E-mail')
    cellphone = models.CharField(
        max_length=14, verbose_name='Número de celular')
    commercial_phone = models.CharField(
        max_length=12, verbose_name='Número comercial')

    def __str__(self):
        return self.company.name

    @property
    def format_cellphone(self):
        return f"({self.cellphone[:2]}) {self.cellphone[2]}{self.cellphone[3:7]}-{self.cellphone[7:]}"

    @property
    def format_phone_commercial(self):
        return f"({self.commercial_phone[:2]}) {self.commercial_phone[2:6]}-{self.commercial_phone[6:]}"


class Requirements(models.Model):
    name = models.CharField(
        max_length=45, null=False, verbose_name='Tipo de requisito')

    def __str__(self):
        return self.name

    @property
    def format_requirement(self):
        return f"{self.name}".capitalize()


class Jobs(models.Model):
    company = models.CharField(
        max_length=255, null=False, verbose_name='Empresa contratante')
    title = models.CharField(max_length=255, null=False,
                             verbose_name='Título da vaga')
    requirements = models.ManyToManyField(
        Requirements, verbose_name='Requisitos')
    salary_range = models.CharField(
        max_length=45, null=False, choices=SALARY_CHOICES,
        verbose_name='Faixa salarial')
    description = models.TextField(
        null=False, max_length=255, verbose_name='Descrição da vaga')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
