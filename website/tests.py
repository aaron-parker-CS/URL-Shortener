from unittest.mock import Mock

from django.test import TestCase, Client
from .models import Website


# Create your tests here.
class Test_URL_Redirect(TestCase):
    new_model = None
    test_client = None

    def setUp(self):
        self.test_client = Client()
        self.new_model = Website(full_url='https://www.red.com', short_url='urltest')
        self.new_model.save()

    def test_add_new(self):
        new_site = Website(full_url='https://www.google.com', short_url='example')
        new_site.save()
        self.assertEqual(True, Website.objects.filter(id=new_site.id), msg="Website fails to save into the database")

    def test_redirect(self):
        resp = self.test_client.get(self.new_model.short_url)
        self.assertRedirects(resp, self.new_model.full_url)

    def test_post(self):
        resp = self.test_client.post('/', {'full': 'https://www.yahoo.com/'})
        self.assertEqual(resp.context['full'], 'https://www.yahoo.com/',
                         msg='Error in POST, full url is not being displayed.')
