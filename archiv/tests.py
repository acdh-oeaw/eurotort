import json
from datetime import date

from django.apps import apps
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from archiv.dal_urls import urlpatterns
from archiv.models import Court, CourtDecission, PartialLegalSystem, Tag

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

    def test_017_ac_keyword(self):
        url = reverse("archiv-ac:keyword-autocomplete")
        response = client.get(f"{url}?q=o")
        self.assertTrue("text-bg-primary" in str(response.content))

    def test_018_ac_tag(self):
        Tag.objects.get_or_create(tag="test tag")
        url = reverse("archiv-ac:tag-autocomplete")
        response = client.get(f"{url}?q=t")
        self.assertTrue("text-bg-success" in str(response.content))

    def test_conditional_ac(self):
        pl_system_a = PartialLegalSystem.objects.create(name="Constraint LS A")
        pl_system_b = PartialLegalSystem.objects.create(name="Constraint LS B")

        court_a = Court.objects.create(
            name="ConstraintCourt Alpha", partial_legal_system=pl_system_a
        )
        court_b = Court.objects.create(
            name="ConstraintCourt Beta", partial_legal_system=pl_system_b
        )
        court_c = Court.objects.create(
            name="ConstraintCourt Gamma", partial_legal_system=pl_system_a
        )

        url = reverse("archiv-ac:court-autocomplete")

        response = client.get(
            url,
            {
                "q": "ConstraintCourt",
                "forward": json.dumps({"partial_legal_system": str(pl_system_a.id)}),
            },
        )
        self.assertEqual(response.status_code, 200)
        ids = {int(item["id"]) for item in response.json()["results"]}
        self.assertSetEqual(ids, {court_a.id, court_c.id})

        response = client.get(
            url,
            {
                "q": "ConstraintCourt",
                "forward": json.dumps(
                    {
                        "partial_legal_system": [
                            str(pl_system_a.id),
                            str(pl_system_b.id),
                        ]
                    }
                ),
            },
        )
        self.assertEqual(response.status_code, 200)
        ids = {int(item["id"]) for item in response.json()["results"]}
        self.assertSetEqual(ids, {court_a.id, court_b.id, court_c.id})

    def test_019_courtdecission_str_all_cases(self):
        court = Court.objects.create(name="StringTest Court")
        decission_date = date(2024, 1, 31)

        # file_number + party branch
        case = CourtDecission.objects.create(
            court=court,
            decission_date=decission_date,
            party="Alice v. Bob",
            file_number="A-123/24",
        )
        self.assertEqual(
            str(case), "Alice v. Bob, StringTest Court 31 Jan 2024 A-123/24"
        )

        # file_number + court + decission_date branch
        case = CourtDecission.objects.create(
            court=court,
            decission_date=decission_date,
            file_number="B-777/24",
        )
        self.assertEqual(str(case), "StringTest Court 31 Jan 2024, B-777/24")

        # party + court + decission_date branch
        case = CourtDecission.objects.create(
            court=court,
            decission_date=decission_date,
            party="Carol v. Dave",
        )
        self.assertEqual(str(case), "Carol v. Dave, StringTest Court 31 Jan 2024")

        # court + decission_date branch
        case = CourtDecission.objects.create(
            court=court,
            decission_date=decission_date,
        )
        self.assertEqual(str(case), "StringTest Court 31 Jan 2024")

        # fallback branch
        case = CourtDecission.objects.create()
        self.assertEqual(str(case), str(case.id))

        # sample object with missing decission_date and file_number + party set
        # exercises whitespace normalization when date is empty.
        case = CourtDecission.objects.create(
            court=court,
            party="Erin v. Frank",
            file_number="C-55/24",
            decission_date=None,
        )
        self.assertEqual(str(case), "Erin v. Frank, StringTest Court C-55/24")

        # current behavior: missing court while file_number + party are set raises.
        case = CourtDecission.objects.create(
            party="No Court v. Someone",
            file_number="NC-1",
        )
        with self.assertRaises(AttributeError):
            str(case)

    def test_020_courtdecission_detail_context_data_motto_paragraphs(self):
        case = CourtDecission.objects.create(
            motto="First paragraph.\n\nSecond paragraph."
        )

        response = client.get(case.get_absolute_url(), {"pk": case.id})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["decision_paragraphs"],
            ["First paragraph.", "Second paragraph."],
        )

    def test_021_courtdecission_detail_context_data_empty_motto(self):
        case = CourtDecission.objects.create(motto="")

        response = client.get(case.get_absolute_url(), {"pk": case.id})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["decision_paragraphs"], [])

    def test_022_courtdecission_detail_context_data_missing_motto(self):
        case = CourtDecission.objects.create()

        response = client.get(case.get_absolute_url(), {"pk": case.id})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["decision_paragraphs"], [])
