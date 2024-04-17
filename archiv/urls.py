# generated by appcreator
from django.urls import path

from . import views

app_name = "archiv"
urlpatterns = [
    path("court/", views.CourtListView.as_view(), name="court_browse"),
    path("court/detail/<int:pk>", views.CourtDetailView.as_view(), name="court_detail"),
    path("court/create/", views.CourtCreate.as_view(), name="court_create"),
    path("court/edit/<int:pk>", views.CourtUpdate.as_view(), name="court_edit"),
    path("court/delete/<int:pk>", views.CourtDelete.as_view(), name="court_delete"),
    path("yearbook/", views.YearBookListView.as_view(), name="yearbook_browse"),
    path(
        "yearbook/detail/<int:pk>",
        views.YearBookDetailView.as_view(),
        name="yearbook_detail",
    ),
    path("yearbook/create/", views.YearBookCreate.as_view(), name="yearbook_create"),
    path(
        "yearbook/edit/<int:pk>", views.YearBookUpdate.as_view(), name="yearbook_edit"
    ),
    path(
        "yearbook/delete/<int:pk>",
        views.YearBookDelete.as_view(),
        name="yearbook_delete",
    ),
    path(
        "case/",
        views.CourtDecissionListView.as_view(),
        name="courtdecission_browse",
    ),
    path(
        "case/detail/<int:pk>",
        views.CourtDecissionDetailView.as_view(),
        name="courtdecission_detail",
    ),
    path(
        "case/create/",
        views.CourtDecissionCreate.as_view(),
        name="courtdecission_create",
    ),
    path(
        "case/edit/<int:pk>",
        views.CourtDecissionUpdate.as_view(),
        name="courtdecission_edit",
    ),
    path(
        "case/delete/<int:pk>",
        views.CourtDecissionDelete.as_view(),
        name="courtdecission_delete",
    ),
    path("keyword/", views.KeyWordListView.as_view(), name="keyword_browse"),
    path(
        "keyword/detail/<int:pk>",
        views.KeyWordDetailView.as_view(),
        name="keyword_detail",
    ),
    path("keyword/create/", views.KeyWordCreate.as_view(), name="keyword_create"),
    path("keyword/edit/<int:pk>", views.KeyWordUpdate.as_view(), name="keyword_edit"),
    path(
        "keyword/delete/<int:pk>", views.KeyWordDelete.as_view(), name="keyword_delete"
    ),
    path(
        "partiallegalsystem/",
        views.PartialLegalSystemListView.as_view(),
        name="partiallegalsystem_browse",
    ),
    path(
        "partiallegalsystem/detail/<int:pk>",
        views.PartialLegalSystemDetailView.as_view(),
        name="partiallegalsystem_detail",
    ),
    path(
        "partiallegalsystem/create/",
        views.PartialLegalSystemCreate.as_view(),
        name="partiallegalsystem_create",
    ),
    path(
        "partiallegalsystem/edit/<int:pk>",
        views.PartialLegalSystemUpdate.as_view(),
        name="partiallegalsystem_edit",
    ),
    path(
        "partiallegalsystem/delete/<int:pk>",
        views.PartialLegalSystemDelete.as_view(),
        name="partiallegalsystem_delete",
    ),
    path("person/", views.PersonListView.as_view(), name="person_browse"),
    path(
        "person/detail/<int:pk>", views.PersonDetailView.as_view(), name="person_detail"
    ),
    path("person/create/", views.PersonCreate.as_view(), name="person_create"),
    path("person/edit/<int:pk>", views.PersonUpdate.as_view(), name="person_edit"),
    path("person/delete/<int:pk>", views.PersonDelete.as_view(), name="person_delete"),
    path("tag/", views.TagListView.as_view(), name="tag_browse"),
    path("tag/detail/<int:pk>", views.TagDetailView.as_view(), name="tag_detail"),
    path("tag/create/", views.TagCreate.as_view(), name="tag_create"),
    path("tag/edit/<int:pk>", views.TagUpdate.as_view(), name="tag_edit"),
    path("tag/delete/<int:pk>", views.TagDelete.as_view(), name="tag_delete"),
]
