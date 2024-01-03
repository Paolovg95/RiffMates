from django.test import TestCase

# Create your tests here.
class TestHome(TestCase):
    def test_credits(self):
        # calls a view through the URL routing system
        response = self.client.get("/credits/")
        self.assertEqual(200, response.status_code)
