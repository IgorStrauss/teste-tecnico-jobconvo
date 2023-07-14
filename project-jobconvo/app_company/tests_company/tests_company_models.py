import pytest
from app_candidate.models import Experience
from app_company.models import Company
from django.contrib.auth.models import User
from django.test import TestCase


class TestCompanyTestCase(TestCase):
    def setUp(self) -> None:
        self.company = Company.objects.create(
            name="company_name",
            cnpj='00000000000000')

    def test_company_name(self):
        self.assertEqual(self.company.name, "company_name")

    def test_company_return_str(self):
        expected_str = "company_name"
        actual_str = str(self.company)
        self.assertEqual(actual_str, expected_str)
