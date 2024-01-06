from django.apps import apps
from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import Client
from django.test import TestCase
from django.urls import reverse

from archiv.dal_urls import urlpatterns
from archiv.models import CourtDecission
from archiv.models import YearBook

MODELS = list(apps.all_models["archiv"].values())

client = Client()
USER = {"username": "testuser", "password": "somepassword"}


class ArchivTestCase(TestCase):
    fixtures = ["dump.json"]

    def setUp(self):
        # Create two users
        User.objects.create_user(**USER)

    def test_001_filterview(self):
        url = CourtDecission.get_listview_url()
        response = client.get(f"{url}?ft_search=King)")
        self.assertEqual(response.status_code, 200)
        response = client.get(f"{url}?ft_search=King*)")
        self.assertEqual(response.status_code, 200)

    def test_002_listviews(self):
        for x in MODELS:
            try:
                url = x.get_listview_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url)
                self.assertEqual(response.status_code, 200)
        client.login(**USER)
        for x in MODELS:
            try:
                url = x.get_listview_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_003_detailviews(self):
        for x in MODELS:
            item = x.objects.first()
            try:
                url = item.get_absolute_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {"pk": item.id})
                self.assertEqual(response.status_code, 200)

    def test_004_editviews(self):
        client.login(**USER)
        for x in MODELS:
            item = x.objects.first()
            try:
                url = item.get_edit_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {"pk": item.id})
                self.assertEqual(response.status_code, 200)

    def test_005_createviews_not_logged_in(self):
        for x in MODELS:
            item = x.objects.first()
            try:
                url = item.get_createview_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {"pk": item.id})
                self.assertEqual(response.status_code, 302)

    def test_006_createviews_logged_in(self):
        client.login(**USER)
        for x in MODELS:
            item = x.objects.first()
            try:
                url = item.get_createview_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {"pk": item.id})
                self.assertEqual(response.status_code, 200)

    def test_007_save_courtdecission(self):
        dummy = {
            "short_description": "King of Queens",
            "motto": "Malcom in the middle.",
            "commentary": "The <strong>Simpsons</strong>!",
        }
        new_court = CourtDecission.objects.create(**dummy)
        full_text = new_court.full_text
        self.assertTrue("Simpsons" in full_text)
        self.assertFalse("<strong>" in full_text)

    def test_016_ac_views(self):
        ns = "archiv-ac"
        for x in urlpatterns:
            url_name = f"{ns}:{x.name}"
            url = f"{reverse(url_name)}?q=hansi"
            response = client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTrue("results" in response.json().keys())

    def test_017_yearbook_part_of(self):
        for x in YearBook.objects.exclude(has_bibliographic_items=None):
            x.delete()
        call_command("yearbook_parent")
        self.assertFalse(
            YearBook.objects.filter(has_bibliographic_items=None).filter(part_of=None)
        )
