from django.test import TestCase
from django.urls import reverse


class UrlsTestApp(TestCase):
    def test_test(self):
        assert 1 != 2

    def test_url_home_candidate_is_correct(self):
        index_url = reverse('home')
        self.assertEqual(index_url, '/')
