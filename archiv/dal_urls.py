# generated by appcreator
from django.urls import path

from . import dal_views

app_name = "archiv"
urlpatterns = [
    path("court-autocomplete", dal_views.CourtAC.as_view(), name="court-autocomplete"),
    path(
        "courtdecission-autocomplete",
        dal_views.CourtDecissionAC.as_view(),
        name="courtdecission-autocomplete",
    ),
    path(
        "keyword-autocomplete",
        dal_views.KeyWordAC.as_view(),
        name="keyword-autocomplete",
    ),
    path(
        "partiallegalsystem-autocomplete",
        dal_views.PartialLegalSystemAC.as_view(),
        name="partiallegalsystem-autocomplete",
    ),
    path(
        "person-autocomplete", dal_views.PersonAC.as_view(), name="person-autocomplete"
    ),
    path(
        "tag-autocomplete",
        dal_views.TagAC.as_view(create_field="tag", validate_create=True),
        name="tag-autocomplete",
    ),
    path(
        "tag-filter-autocomplete",
        dal_views.TagAC.as_view(),
        name="tag-no-filter-autocomplete",
    ),
    path(
        "yearbook-autocomplete",
        dal_views.YearBookAC.as_view(),
        name="yearbook-autocomplete",
    ),
    path(
        "monograph-autocomplete",
        dal_views.MonographAC.as_view(),
        name="monograph-autocomplete",
    ),
    path(
        "chapter-autocomplete",
        dal_views.ChapterAC.as_view(),
        name="chapter-autocomplete",
    ),
]
