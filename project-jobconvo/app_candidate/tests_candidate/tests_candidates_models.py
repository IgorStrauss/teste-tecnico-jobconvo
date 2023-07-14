from app_candidate.models import Experience
from django.contrib.auth.models import User
from django.test import TestCase


class TestExperienceTestCase(TestCase):

    def setUp(self) -> None:
        self.experience = Experience.objects.create(
            user=User.objects.create_user(
                id=1,
                username="user",
                email="email",
            ),
            name="name",
            description="description",
        )

    def test_experience_name(self):
        self.assertEqual(self.experience.name, "name")

    def test_experience_description(self):
        self.assertEqual(self.experience.description, "description")

    def test_experience_return_str(self):
        expected_str = "name"
        actual_str = str(self.experience)
        self.assertEqual(actual_str, expected_str)
