""" tests """

from django.test import TestCase, Client
from django.contrib.auth.models import User


class AuthorizationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.authenticated_user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            is_staff=False,
            is_superuser=False,
        )
        self.urls = ["/nyrecension", "/profile"]

    def test_access_by_authenticated_user(self):
        self.client.login(username="testuser", password="testpassword")

        for url in self.urls:
            response = self.client.get(url)
            # Assuming that an authenticated user can access all pages
            self.assertEqual(
                response.status_code, 200, f"Authenticated user could not access {url}"
            )

    def test_access_by_anonymous_user(self):
        self.client.logout()

        for url in self.urls:
            response = self.client.get(url)
            self.assertEqual(
                response.status_code, 302, f"Anonymous user could access {url}"
            )
