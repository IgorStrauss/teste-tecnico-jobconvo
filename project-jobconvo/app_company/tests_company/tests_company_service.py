import pytest
from app_candidate.models import Experience
from app_company.models import Company
from app_company.service_candidate import CandidateDetailView
from django.contrib.auth.models import User
from django.test import TestCase


class TestCandidateDetailViewTestCase(TestCase):
    def setUp(self):
        self.candidate = User.objects.create_user(
            id=1,
            first_name='first_name',
            last_name='last_name',
            username='username',
            email='email',
            password='password',
        )

    def test_get_context_data(self):
        ...
