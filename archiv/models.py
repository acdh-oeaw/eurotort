# generated by appcreator

from django.db import models
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex
from django.urls import reverse
from django.utils.html import strip_tags
from next_prev import next_in_order, prev_in_order
from browsing.browsing_utils import model_to_dict


def set_extra(self, **kwargs):
    self.extra = kwargs
    return self


models.Field.set_extra = set_extra


class YearBook(models.Model):
    """Yearbook"""

    title = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="Title",
        help_text="Title",
    ).set_extra(
        is_public=True,
        arche_prop="hasTitle",
    )

    class Meta:
        ordering = [
            "title",
        ]
        verbose_name = "Yearbook"

    def __str__(self):
        if self.title:
            return f"{self.title}"
        else:
            return f"{self.id}, no title provided"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse("archiv:yearbook_browse")

    @classmethod
    def get_natural_primary_key(self):
        return "title"

    @classmethod
    def get_createview_url(self):
        return reverse("archiv:yearbook_create")

    def get_absolute_url(self):
        return reverse("archiv:yearbook_detail", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("archiv:yearbook_delete", kwargs={"pk": self.id})

    def get_edit_url(self):
        return reverse("archiv:yearbook_edit", kwargs={"pk": self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return reverse("archiv:yearbook_detail", kwargs={"pk": next.id})
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return reverse("archiv:yearbook_detail", kwargs={"pk": prev.id})
        return False


class Court(models.Model):
    """Court"""

    legacy_id = models.CharField(max_length=300, blank=True, verbose_name="Legacy ID")
    legacy_pk = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Primärschlüssel Alt",
        help_text="Primärschlüssel Alt",
    ).set_extra(
        is_public=False,
        data_lookup="Gericht_Id",
        arche_prop="hasNonLinkedIdentifier",
    )
    name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Name",
        help_text="Name",
    ).set_extra(
        is_public=True,
        data_lookup="Gericht_Bezeichnung",
        arche_prop="hasTitle",
    )
    abbreviation = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Abbreviation",
        help_text="Abbreviation",
    ).set_extra(
        is_public=True,
        data_lookup="Gericht_Kurzbezeichnung",
        arche_prop="hasAlternativeTitle",
    )
    is_high_court = models.BooleanField(
        default=False,
        blank=True,
        null=True,
        verbose_name="High Court",
        help_text="High Court",
    ).set_extra(
        is_public=True,
        data_lookup="Abbreviation",
    )
    partial_legal_system = models.ForeignKey(
        "PartialLegalSystem",
        related_name="rvn_court_partial_legal_system_partiallegalsystem",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Partial Legal System",
        help_text="Partial Legal System",
    ).set_extra(
        is_public=True,
        data_lookup="Gericht_Teilrechtsordnung",
    )
    orig_data_csv = models.TextField(
        blank=True, null=True, verbose_name="The original data"
    ).set_extra(is_public=True)

    class Meta:
        ordering = [
            "name",
        ]
        verbose_name = "Court"

    def __str__(self):
        if self.name:
            return f"{self.name}"
        else:
            return f"{self.id}"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse("archiv:court_browse")

    @classmethod
    def get_source_table(self):
        return "tb_gericht.csv"

    @classmethod
    def get_natural_primary_key(self):
        return "legacy_pk"

    @classmethod
    def get_createview_url(self):
        return reverse("archiv:court_create")

    def get_absolute_url(self):
        return reverse("archiv:court_detail", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("archiv:court_delete", kwargs={"pk": self.id})

    def get_edit_url(self):
        return reverse("archiv:court_edit", kwargs={"pk": self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return reverse("archiv:court_detail", kwargs={"pk": next.id})
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return reverse("archiv:court_detail", kwargs={"pk": prev.id})
        return False


class CourtDecission(models.Model):
    """CourtDecission"""

    legacy_id = models.CharField(max_length=300, blank=True, verbose_name="Legacy ID")
    legacy_pk = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Primärschlüssel Alt",
        help_text="Primärschlüssel Alt",
    ).set_extra(
        is_public=False,
        data_lookup="Entscheidung_Id",
        arche_prop="hasNonLinkedIdentifier",
    )
    partial_legal_system = models.ForeignKey(
        "PartialLegalSystem",
        related_name="rvn_courtdecission_partial_legal_system_partiallegalsystem",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="PartialLegalSystem",
        help_text="PartialLegalSystem",
    ).set_extra(
        is_public=True,
        data_lookup="Entscheidung_Teilrechtsordnung",
    )
    court = models.ForeignKey(
        "Court",
        related_name="rvn_courtdecission_court_court",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Court",
        help_text="Court",
    ).set_extra(
        is_public=True,
        data_lookup="Entscheidung_Gericht",
    )
    decission_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Date",
        help_text="Date",
    ).set_extra(
        is_public=True,
        data_lookup="Entscheidung_Datum",
    )
    file_number = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="File Number",
        help_text="File Number",
    ).set_extra(
        is_public=True,
        data_lookup="Entscheidung_Aktenzahl",
        arche_prop="hasNonLinkedIdentifier",
    )
    party = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Parties",
        help_text="Parties",
    ).set_extra(
        is_public=True,
        data_lookup="Entscheidung_Parteien",
    )
    location = models.TextField(
        blank=True,
        null=True,
        verbose_name="Decission Location",
        help_text="Decission Location",
    ).set_extra(
        is_public=True,
        data_lookup="Entscheidung_Fundstelle",
    )
    year_book_title = models.ForeignKey(
        "YearBook",
        related_name="related_court_decission",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Year Book",
        help_text="Published in Year Book",
    )
    year_book_issue = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name="Year Book Issue/Page",
        help_text="Issue/Page",
    )
    short_description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Short Description",
        help_text="Short Description",
    ).set_extra(
        is_public=True,
        data_lookup="Entscheidung_Kurzbeschreibung",
        arche_prop="hasDescription",
    )
    situation = models.TextField(
        blank=True,
        null=True,
        verbose_name="Sachverhalt",
        help_text="Sachverhalt",
    ).set_extra(
        is_public=True,
        data_lookup="Entscheidung_Sachverhalt",
    )
    motto = models.TextField(
        blank=True,
        null=True,
        verbose_name="Leitsatz",
        help_text="Sachverhalt",
    ).set_extra(
        is_public=True,
        data_lookup="Entscheidung_Leitsatz",
    )
    commentary = models.TextField(
        blank=True,
        null=True,
        verbose_name="Kommentar",
        help_text="Kommentar",
    ).set_extra(
        is_public=True,
        data_lookup="Entscheidung_Kommentar",
    )
    additional_information = models.TextField(
        blank=True,
        null=True,
        verbose_name="Zusatzinfo",
        help_text="Zusatzinfo",
    ).set_extra(
        is_public=True,
        data_lookup="Entscheidung_Zusatzinfo",
    )
    keyword = models.ManyToManyField(
        "KeyWord",
        related_name="rvn_courtdecission_keyword_keyword",
        blank=True,
        verbose_name="Keywords",
        help_text="Keywords",
    ).set_extra(
        is_public=True,
        arche_prop="hasAuthor",
    )
    author = models.ManyToManyField(
        "Person",
        related_name="rvn_courtdecission_author_person",
        blank=True,
        verbose_name="AutorIn",
        help_text="AutorIn",
    ).set_extra(
        is_public=True,
        arche_prop="hasSubject",
    )
    orig_data_csv = models.TextField(
        blank=True, null=True, verbose_name="The original data"
    ).set_extra(is_public=True)
    full_text = models.TextField(
        blank=True,
        null=True,
        verbose_name="Fulltext field",
        help_text="Fulltext field (technical field)",
    )
    vector_column = SearchVectorField(null=True)

    class Meta:
        ordering = [
            "id",
        ]
        verbose_name = "CourtDecission"
        indexes = (GinIndex(fields=["vector_column"]),)

    def save(self, *args, **kwargs):
        self.full_text = self.join_search_fields()
        super(CourtDecission, self).save(*args, **kwargs)

    def __str__(self):
        if self.file_number and self.party:
            return f"{self.file_number},»{self.party}«"
        elif self.file_number:
            return f"{self.file_number}"
        else:
            return f"{self.id}"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def search_field_names(self):
        text_fields = [
            "short_description",
            "situation",
            "motto",
            "commentary",
            "additional_information",
        ]
        return text_fields

    def join_search_fields(self):
        full_text = set(
            [
                getattr(self, x, "")
                for x in self.search_field_names()
                if getattr(self, x, None) is not None
            ]
        )
        full_text_str = " ".join(
            [x for x in full_text if isinstance(x, str) and x != "nan"]
        )
        return " ".join(f"{strip_tags(full_text_str)} {self.id}".split())

    @classmethod
    def get_listview_url(self):
        return reverse("archiv:courtdecission_browse")

    @classmethod
    def get_source_table(self):
        return "tb_entscheidungen.csv"

    @classmethod
    def get_natural_primary_key(self):
        return "legacy_pk"

    @classmethod
    def get_createview_url(self):
        return reverse("archiv:courtdecission_create")

    def get_absolute_url(self):
        return reverse("archiv:courtdecission_detail", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("archiv:courtdecission_delete", kwargs={"pk": self.id})

    def get_edit_url(self):
        return reverse("archiv:courtdecission_edit", kwargs={"pk": self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return reverse("archiv:courtdecission_detail", kwargs={"pk": next.id})
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return reverse("archiv:courtdecission_detail", kwargs={"pk": prev.id})
        return False


class KeyWord(models.Model):
    """KeyWord"""

    legacy_id = models.CharField(max_length=300, blank=True, verbose_name="Legacy ID")
    legacy_pk = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Primärschlüssel Alt",
        help_text="Primärschlüssel Alt",
    ).set_extra(
        is_public=False,
        data_lookup="Stichwort_Id",
        arche_prop="hasNonLinkedIdentifier",
    )
    name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Name",
        help_text="Name",
    ).set_extra(
        is_public=True,
        data_lookup="Stichwort_Bezeichnung",
        arche_prop="hasTitle",
    )
    part_of = models.ForeignKey(
        "KeyWord",
        related_name="rvn_keyword_part_of_keyword",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Parent",
        help_text="Parent",
    ).set_extra(
        is_public=True,
        data_lookup="Stichwort_Parent",
    )
    orig_data_csv = models.TextField(
        blank=True, null=True, verbose_name="The original data"
    ).set_extra(is_public=True)

    class Meta:
        ordering = [
            "name",
        ]
        verbose_name = "KeyWord"

    def __str__(self):
        if self.name and self.part_of:
            return f"{self.part_of} >> {self.name}"
        elif self.name:
            return f"{self.name}"
        else:
            return f"{self.id}"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse("archiv:keyword_browse")

    @classmethod
    def get_source_table(self):
        return "tb_stichworte.csv"

    @classmethod
    def get_natural_primary_key(self):
        return "legacy_pk"

    @classmethod
    def get_createview_url(self):
        return reverse("archiv:keyword_create")

    def get_absolute_url(self):
        return reverse("archiv:keyword_detail", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("archiv:keyword_delete", kwargs={"pk": self.id})

    def get_edit_url(self):
        return reverse("archiv:keyword_edit", kwargs={"pk": self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return reverse("archiv:keyword_detail", kwargs={"pk": next.id})
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return reverse("archiv:keyword_detail", kwargs={"pk": prev.id})
        return False


class PartialLegalSystem(models.Model):
    """PartialLegalSystem"""

    legacy_id = models.CharField(max_length=300, blank=True, verbose_name="Legacy ID")
    legacy_pk = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Primärschlüssel Alt",
        help_text="Primärschlüssel Alt",
    ).set_extra(
        is_public=True,
        data_lookup="Teilrecht_Id",
        arche_prop="hasNonLinkedIdentifier",
    )
    name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="name",
        help_text="name",
    ).set_extra(
        is_public=True,
        data_lookup="Teilrecht_Bezeichnung",
    )
    orig_data_csv = models.TextField(
        blank=True, null=True, verbose_name="The original data"
    ).set_extra(is_public=True)

    class Meta:
        ordering = [
            "id",
        ]
        verbose_name = "PartialLegalSystem"

    def __str__(self):
        if self.name:
            return f"{self.name}"
        else:
            return f"{self.id}"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse("archiv:partiallegalsystem_browse")

    @classmethod
    def get_source_table(self):
        return "tb_teilrechtsordnung.csv"

    @classmethod
    def get_natural_primary_key(self):
        return "legacy_pk"

    @classmethod
    def get_createview_url(self):
        return reverse("archiv:partiallegalsystem_create")

    def get_absolute_url(self):
        return reverse("archiv:partiallegalsystem_detail", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("archiv:partiallegalsystem_delete", kwargs={"pk": self.id})

    def get_edit_url(self):
        return reverse("archiv:partiallegalsystem_edit", kwargs={"pk": self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return reverse("archiv:partiallegalsystem_detail", kwargs={"pk": next.id})
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return reverse("archiv:partiallegalsystem_detail", kwargs={"pk": prev.id})
        return False


class Person(models.Model):
    """Person"""

    legacy_id = models.CharField(max_length=300, blank=True, verbose_name="Legacy ID")
    legacy_pk = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Primärschlüssel Alt",
        help_text="Primärschlüssel Alt",
    ).set_extra(
        is_public=False,
        data_lookup="Autor_Id",
        arche_prop="hasNonLinkedIdentifier",
    )
    last_name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Last Name",
        help_text="Last Name",
    ).set_extra(
        is_public=True,
        data_lookup="Autor_Nachname",
        arche_prop="hasLastName",
    )
    first_name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="First Name",
        help_text="First Name",
    ).set_extra(
        is_public=True,
        data_lookup="Autor_Vorname",
        arche_prop="hasFirstName",
    )
    legal_system = models.ManyToManyField(
        "PartialLegalSystem",
        related_name="has_related_author",
        blank=True,
        verbose_name="Legalsystem",
        help_text="Legalsystem",
    ).set_extra(
        is_public=True,
        arche_prop="hasAuthor",
    )
    contact = models.EmailField(
        blank=True,
        verbose_name="Contact",
        help_text="Email address"
    )
    orcid = models.URLField(
        blank=True,
        verbose_name="ORCID",
        help_text="ORCID (as URL)"
    ).set_extra(
        is_public=True,
        arche_prop="hasIdentifier",
    )
    orig_data_csv = models.TextField(
        blank=True, null=True, verbose_name="The original data"
    ).set_extra(is_public=True)

    class Meta:
        ordering = [
            "last_name",
        ]
        verbose_name = "Person"

    def __str__(self):
        if self.last_name and self.first_name:
            return f"{self.last_name}, {self.first_name}"
        else:
            return f"{ſelf.last_name}"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse("archiv:person_browse")

    @classmethod
    def get_source_table(self):
        return "tb_autor.csv"

    @classmethod
    def get_natural_primary_key(self):
        return "legacy_pk"

    @classmethod
    def get_createview_url(self):
        return reverse("archiv:person_create")

    def get_absolute_url(self):
        return reverse("archiv:person_detail", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("archiv:person_delete", kwargs={"pk": self.id})

    def get_edit_url(self):
        return reverse("archiv:person_edit", kwargs={"pk": self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return reverse("archiv:person_detail", kwargs={"pk": next.id})
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return reverse("archiv:person_detail", kwargs={"pk": prev.id})
        return False
