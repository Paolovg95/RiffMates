from django.test import TestCase
from bands.models import Musician
from datetime import date
# Create your tests here.
class TestBand(TestCase):
    def setUp(self):
        self.musician = Musician.objects.create(first_name="First", last_name="Last", birth_date=date(1990,1,1))

    def test_get_musician(self):
        url = f"/bands/musician/{self.musician.id}/"
        response = self.client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertEqual(response.context['musician'].id, self.musician.id)
        # context = ContextList type
        # context['musician'] = Musician Class type
        self.assertIn(self.musician.first_name, response.content.decode())
        self.assertIn(self.musician.last_name, response.content.decode())
