# generated by appcreator
import django_tables2 as tables
from browsing.utils import MergeColumn

from .models import Court
from .models import CourtDecission
from .models import KeyWord
from .models import PartialLegalSystem
from .models import Person
from .models import Tag
from .models import YearBook


class ResultsTable(tables.Table):
    id = tables.LinkColumn(verbose_name="ID")
    full_text = tables.columns.TemplateColumn(
        template_code="{{ record.full_text|safe }}"
    )

    class Meta:
        model = CourtDecission
        fields = (
            "id",
            "date_written",
            "full_text",
        )
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}


class YearBookTable(tables.Table):
    id = tables.LinkColumn(verbose_name="ID")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = YearBook
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}


class CourtTable(tables.Table):
    id = tables.LinkColumn(verbose_name="ID")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = Court
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}


class CourtDecissionTable(tables.Table):
    id = tables.LinkColumn(verbose_name="ID")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")
    keyword = tables.columns.ManyToManyColumn(verbose_name="Keywords")
    author = tables.columns.ManyToManyColumn(verbose_name="Authors")
    related_decision = tables.columns.ManyToManyColumn(verbose_name="Related decisions")
    tag = tables.columns.ManyToManyColumn(verbose_name="Tags")
    kwic = tables.columns.TemplateColumn(
        template_code="{{ record.kwic|safe }}",
        verbose_name="Keyword in Context",
        orderable=False,
    )

    class Meta:
        model = CourtDecission
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}


class KeyWordTable(tables.Table):
    id = tables.LinkColumn(verbose_name="ID")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = KeyWord
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}


class PartialLegalSystemTable(tables.Table):
    id = tables.LinkColumn(verbose_name="ID")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = PartialLegalSystem
        sequence = ("id", "name")
        attrs = {"class": "table table-responsive table-hover"}


class PersonTable(tables.Table):
    id = tables.LinkColumn(verbose_name="ID")
    legal_system = tables.columns.ManyToManyColumn(verbose_name="Legal system")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = Person
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}


class TagTable(tables.Table):
    id = tables.LinkColumn(verbose_name="ID")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = Tag
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}
