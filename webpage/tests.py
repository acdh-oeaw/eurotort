from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from django.test import TestCase


class WebpageTest(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user("temporary", "temp@gmail.com", "temporary")

    def test_webpage(self):
        rv = self.client.get("/")
        self.assertEqual(rv.status_code, 200)
        self.assertContains(rv, "Eurotort")
        rv = self.client.get("/accounts/login/")
        self.assertContains(rv, "Username")
        form_data = {"username": "temporary", "password": "temporary"}
        rv = self.client.post("/accounts/login/", form_data, follow=True)
        rv = self.client.get("/logout/", follow=True)
        self.assertContains(rv, "Sayōnara")
        form_data = {"username": "non_exist", "password": "temporary"}
        rv = self.client.post("/accounts/login/", form_data, follow=True)
        self.assertContains(rv, "user does not exist")

    def test_imprint_view(self):

        rv = self.client.get(reverse("webpage:imprint"))
        self.assertEqual(rv.status_code, 200)
        self.assertContains(rv, "Austrian media law")
