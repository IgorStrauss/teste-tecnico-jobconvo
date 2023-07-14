from django.test import Client, TestCase


class HomeViewTest(TestCase):
    def test_home_view(self):
        client = Client()
        response = client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
