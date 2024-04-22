# generated by appcreator
import django_filters
from dal import autocomplete
from django.contrib.postgres.search import SearchHeadline
from django.contrib.postgres.search import SearchQuery
from django.contrib.postgres.search import SearchRank
from django.db.utils import ProgrammingError

from acdh_django_widgets.widgets import RangeSliderWidget

from .models import Court
from .models import CourtDecission
from .models import KeyWord
from .models import PartialLegalSystem
from .models import Person
from .models import Tag
from .models import YearBook

START_SELECTOR = '<span class="text-nowrap bg-warning border-warning rounded border-5">'


FT_HELPTEXT = """
    <i class="bi bi-info-circle" role="button" title="Click for information about the full text search"
    data-bs-toggle="modal" data-bs-target="#searchInfoModal"></i>
"""


class YearBookListFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=YearBook._meta.get_field("title").help_text,
        label=YearBook._meta.get_field("title").verbose_name,
    )
    part_of = django_filters.ModelMultipleChoiceFilter(
        queryset=YearBook.objects.all(),
        help_text=YearBook._meta.get_field("part_of").help_text,
        label=YearBook._meta.get_field("part_of").verbose_name,
        widget=autocomplete.ModelSelect2Multiple(
            url="archiv-ac:monograph-autocomplete",
        ),
    )
    year = django_filters.RangeFilter(
        help_text=YearBook._meta.get_field("year").help_text,
        label=YearBook._meta.get_field("year").verbose_name,
        widget=RangeSliderWidget(
            attrs={"min": "1990", "max": "2022", "hide_input_fileds": False}
        ),
    )

    class Meta:
        model = YearBook
        fields = [
            "id",
            "title",
            "year",
        ]


class CourtListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Court._meta.get_field("name").help_text,
        label=Court._meta.get_field("name").verbose_name,
    )
    abbreviation = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Court._meta.get_field("abbreviation").help_text,
        label=Court._meta.get_field("abbreviation").verbose_name,
    )

    partial_legal_system = django_filters.ModelMultipleChoiceFilter(
        queryset=PartialLegalSystem.objects.all(),
        help_text=Court._meta.get_field("partial_legal_system").help_text,
        label=Court._meta.get_field("partial_legal_system").verbose_name,
        widget=autocomplete.ModelSelect2Multiple(
            url="archiv-ac:partiallegalsystem-autocomplete",
        ),
    )

    class Meta:
        model = Court
        fields = [
            "id",
            "name",
            "abbreviation",
            "is_high_court",
            "partial_legal_system",
        ]


class CourtDecissionListFilter(django_filters.FilterSet):
    ft_search = django_filters.CharFilter(
        field_name="vector_column",
        method="search_fulltext",
        label="Volltextsuche",
        help_text=FT_HELPTEXT,
    )
    year_book_title = django_filters.ModelMultipleChoiceFilter(
        queryset=YearBook.objects.all(),
        help_text=CourtDecission._meta.get_field("year_book_title").help_text,
        label=CourtDecission._meta.get_field("year_book_title").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:yearbook-autocomplete",
        ),
    )
    tag = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        help_text=CourtDecission._meta.get_field("tag").help_text,
        label=CourtDecission._meta.get_field("tag").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:tag-no-filter-autocomplete",
        ),
    )
    partial_legal_system = django_filters.ModelMultipleChoiceFilter(
        queryset=PartialLegalSystem.objects.all(),
        help_text=CourtDecission._meta.get_field("partial_legal_system").help_text,
        label=CourtDecission._meta.get_field("partial_legal_system").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:partiallegalsystem-autocomplete",
        ),
    )
    court = django_filters.ModelMultipleChoiceFilter(
        queryset=Court.objects.all(),
        help_text=CourtDecission._meta.get_field("court").help_text,
        label=CourtDecission._meta.get_field("court").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:court-autocomplete",
        ),
    )
    file_number = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=CourtDecission._meta.get_field("file_number").help_text,
        label=CourtDecission._meta.get_field("file_number").verbose_name,
    )
    ecli = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=CourtDecission._meta.get_field("ecli").help_text,
        label=CourtDecission._meta.get_field("ecli").verbose_name,
    )
    party = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=CourtDecission._meta.get_field("party").help_text,
        label=CourtDecission._meta.get_field("party").verbose_name,
    )
    location = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=CourtDecission._meta.get_field("location").help_text,
        label=CourtDecission._meta.get_field("location").verbose_name,
    )
    short_description = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=CourtDecission._meta.get_field("short_description").help_text,
        label=CourtDecission._meta.get_field("short_description").verbose_name,
    )
    situation = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=CourtDecission._meta.get_field("situation").help_text,
        label=CourtDecission._meta.get_field("situation").verbose_name,
    )
    motto = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=CourtDecission._meta.get_field("motto").help_text,
        label=CourtDecission._meta.get_field("motto").verbose_name,
    )
    commentary = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=CourtDecission._meta.get_field("commentary").help_text,
        label=CourtDecission._meta.get_field("commentary").verbose_name,
    )
    additional_information = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=CourtDecission._meta.get_field("additional_information").help_text,
        label=CourtDecission._meta.get_field("additional_information").verbose_name,
    )
    keyword = django_filters.ModelMultipleChoiceFilter(
        queryset=KeyWord.objects.all(),
        help_text=CourtDecission._meta.get_field("keyword").help_text,
        label=CourtDecission._meta.get_field("keyword").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:keyword-autocomplete",
            attrs={'data-html': True}
        ),
    )
    author = django_filters.ModelMultipleChoiceFilter(
        queryset=Person.objects.all(),
        help_text=CourtDecission._meta.get_field("author").help_text,
        label=CourtDecission._meta.get_field("author").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:person-autocomplete",
        ),
    )
    decission_date__year = django_filters.RangeFilter(
        help_text="Year of Decision.",
        label=CourtDecission._meta.get_field("decission_date").verbose_name,
        widget=RangeSliderWidget(
            attrs={"min": "1990", "max": "2022", "hide_input_fileds": False}
        ),
    )

    def search_fulltext(self, queryset, field_name, value):
        search_type = "websearch"
        search_term = value
        if value and value.endswith("*"):
            search_type = "raw"
            search_term = value.replace("*", ":*")
            query = SearchQuery(search_term, config="english", search_type=search_type)
            qs = (
                queryset.filter(vector_column=query)
                .annotate(
                    kwic=SearchHeadline(
                        "full_text",
                        query,
                        start_sel=START_SELECTOR,
                        stop_sel="</span>",
                    )
                )
                .annotate(rank=SearchRank("full_text", query))
                .order_by("-rank")
            )
            try:
                qs
            except ProgrammingError:
                print(f"### processed search value: {search_term} is not valid")
                return queryset
        else:
            query = SearchQuery(value, config="english", search_type=search_type)
            qs = (
                queryset.filter(vector_column=query)
                .annotate(
                    kwic=SearchHeadline(
                        "full_text",
                        query,
                        start_sel=START_SELECTOR,
                        stop_sel="</span>",
                    )
                )
                .annotate(rank=SearchRank("full_text", query))
                .order_by("-rank")
            )
        return qs

    class Meta:
        model = CourtDecission
        fields = [
            "id",
            "ft_search",
            "partial_legal_system",
            "court",
            "decission_date__year",
            "file_number",
            "party",
            "location",
            "short_description",
            "situation",
            "motto",
            "commentary",
            "additional_information",
            "keyword",
            "tag",
            "author",
            "year_book_title",
        ]


class KeyWordListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=KeyWord._meta.get_field("name").help_text,
        label=KeyWord._meta.get_field("name").verbose_name,
    )
    part_of = django_filters.ModelMultipleChoiceFilter(
        queryset=KeyWord.objects.all(),
        help_text=KeyWord._meta.get_field("part_of").help_text,
        label=KeyWord._meta.get_field("part_of").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:keyword-autocomplete",
        ),
    )

    class Meta:
        model = KeyWord
        fields = [
            "id",
            "name",
            "part_of",
        ]


class PartialLegalSystemListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=PartialLegalSystem._meta.get_field("name").help_text,
        label=PartialLegalSystem._meta.get_field("name").verbose_name,
    )

    class Meta:
        model = PartialLegalSystem
        fields = [
            "id",
            "name",
        ]


class PersonListFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Person._meta.get_field("last_name").help_text,
        label=Person._meta.get_field("last_name").verbose_name,
    )
    first_name = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Person._meta.get_field("first_name").help_text,
        label=Person._meta.get_field("first_name").verbose_name,
    )
    legal_system = django_filters.ModelMultipleChoiceFilter(
        queryset=PartialLegalSystem.objects.all(),
        help_text=Person._meta.get_field("legal_system").help_text,
        label=Person._meta.get_field("legal_system").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:partiallegalsystem-autocomplete",
        ),
    )

    class Meta:
        model = Person
        fields = [
            "id",
            "last_name",
            "first_name",
            "legal_system",
        ]


class TagListFilter(django_filters.FilterSet):
    tag = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Tag._meta.get_field("tag").help_text,
        label=Tag._meta.get_field("tag").verbose_name,
    )

    class Meta:
        model = Tag
        fields = [
            "id",
            "tag",
        ]
