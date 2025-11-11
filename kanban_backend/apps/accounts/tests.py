from django.test import TestCase
from django.urls import reverse

class HealthCheckTests(TestCase):
    def test_health_check(self):
        response = self.client.get("/api/v1/health/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("status", response.json())
