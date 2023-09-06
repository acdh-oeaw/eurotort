# generated by appcreator
import django_tables2 as tables

from browsing.browsing_utils import MergeColumn
from .models import (
    Country,
    Court,
    CourtDecission,
    KeyWord,
    PartialLegalSystem,
    Person,
    YearBook
)


class YearBookTable(tables.Table):
    id = tables.LinkColumn(verbose_name="ID")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = YearBook
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}


class CountryTable(tables.Table):
    id = tables.LinkColumn(verbose_name="ID")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = Country
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
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}


class PersonTable(tables.Table):
    id = tables.LinkColumn(verbose_name="ID")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = Person
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}
