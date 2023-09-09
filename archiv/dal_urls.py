# generated by appcreator
from django.urls import path
from . import dal_views

app_name = "archiv"
urlpatterns = [
    path(
        "country-autocomplete",
        dal_views.CountryAC.as_view(),
        name="country-autocomplete",
    ),
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
        "yearbook-autocomplete",
        dal_views.YearBookAC.as_view(),
        name="yearbook-autocomplete",
    ),
]
