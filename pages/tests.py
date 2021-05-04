from django.test import SimpleTestCase
from django.urls import reverse

class SimpleTests(SimpleTestCase):
    databases = '__all__'

    def test_about_page_status_code(self):
        response = self.client.get(reverse('pages:about_page'))
        self.assertEqual(response.status_code, 200)