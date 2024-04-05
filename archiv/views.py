import pandas as pd
from browsing.browsing_utils import BaseCreateView
from browsing.browsing_utils import BaseDetailView
from browsing.browsing_utils import BaseUpdateView
from browsing.browsing_utils import GenericListView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView

from .filters import CourtDecissionListFilter
from .filters import CourtListFilter
from .filters import KeyWordListFilter
from .filters import PartialLegalSystemListFilter
from .filters import PersonListFilter
from .filters import TagListFilter
from .filters import YearBookListFilter
from .forms import CourtDecissionFilterFormHelper
from .forms import CourtDecissionForm
from .forms import CourtFilterFormHelper
from .forms import CourtForm
from .forms import KeyWordFilterFormHelper
from .forms import KeyWordForm
from .forms import PartialLegalSystemFilterFormHelper
from .forms import PartialLegalSystemForm
from .forms import PersonFilterFormHelper
from .forms import PersonForm
from .forms import TagFilterFormHelper
from .forms import TagForm
from .forms import YearBookFilterFormHelper
from .forms import YearBookForm
from .models import Court
from .models import CourtDecission
from .models import KeyWord
from .models import PartialLegalSystem
from .models import Person
from .models import Tag
from .models import YearBook
from .tables import CourtDecissionTable
from .tables import CourtTable
from .tables import KeyWordTable
from .tables import PartialLegalSystemTable
from .tables import PersonTable
from .tables import TagTable
from .tables import YearBookTable


class CustomDetailView(BaseDetailView):
    def get_context_data(self, **kwargs):
        context = super(CustomDetailView, self).get_context_data()
        context["verbose_name"] = self.model._meta.verbose_name
        context["verbose_name_plural"] = self.model._meta.verbose_name_plural
        return context


class CustomUpdateView(BaseUpdateView):
    h1 = "Edit"
    template_name = "archiv/custom_create.html"

    def get_context_data(self, **kwargs):
        context = super(CustomUpdateView, self).get_context_data()
        context["h1"] = self.h1
        return context


class CustomCreateView(BaseCreateView):
    h1 = "Create"
    template_name = "archiv/custom_create.html"

    def get_context_data(self, **kwargs):
        context = super(CustomCreateView, self).get_context_data()
        context["h1"] = self.h1
        return context


class CustomListView(GenericListView):
    h1 = "Hallo"
    create_button_text = "Create new item"
    template_name = "archiv/custom_list.html"

    def get_context_data(self, **kwargs):
        context = super(CustomListView, self).get_context_data()
        context["h1"] = self.h1
        context["create_button_text"] = self.create_button_text
        context["verbose_name"] = self.model._meta.verbose_name
        context["verbose_name_plural"] = self.model._meta.verbose_name_plural
        return context


class CourtListView(CustomListView):
    model = Court
    h1 = "Browse courts"
    create_button_text = "Create new court"
    filter_class = CourtListFilter
    formhelper_class = CourtFilterFormHelper
    table_class = CourtTable
    init_columns = [
        "id",
        "name",
    ]
    enable_merge = True

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ["archiv/custom_list.html"]
        else:
            return ["archiv/court_public_list.html"]

    def get_paginate_by(self, queryset):
        if self.request.user.is_authenticated:
            return 50
        else:
            None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            pass
        else:
            properties = [
                "name",
                "name_english",
                "abbreviation",
                "is_high_court",
                "id",
                "partial_legal_system__name",
                "partial_legal_system__id",
            ]
            data = self.model.objects.all().values_list(*properties)
            df = pd.DataFrame(data=data, columns=properties)
            data = {}
            for gr, ndf in df.groupby("partial_legal_system__name"):
                data[gr] = ndf.sort_values(
                    by=["is_high_court", "name"], ascending=[False, True]
                ).to_dict("records")
            context["grouped_items"] = data
        return context


class CourtDetailView(CustomDetailView):
    model = Court
    template_name = "archiv/court_detail.html"


class CourtCreate(CustomCreateView):
    h1 = "Create court"
    model = Court
    form_class = CourtForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CourtCreate, self).dispatch(*args, **kwargs)


class CourtUpdate(CustomUpdateView):
    h1 = "Edit court"
    model = Court
    form_class = CourtForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CourtUpdate, self).dispatch(*args, **kwargs)


class CourtDelete(DeleteView):
    model = Court
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:court_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CourtDelete, self).dispatch(*args, **kwargs)


class CourtDecissionListView(CustomListView):
    model = CourtDecission
    h1 = "Browse cases"
    create_button_text = "Create new case"
    filter_class = CourtDecissionListFilter
    formhelper_class = CourtDecissionFilterFormHelper
    table_class = CourtDecissionTable
    init_columns = ["id", "file_number", "party", "kwic"]
    exclude_columns = ["full_text", "vector_column"]
    enable_merge = True

    def get_queryset(self, **kwargs):
        qs = super(CourtDecissionListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()

        return self.filter.qs.distinct()


class CourtDecissionDetailView(CustomDetailView):
    model = CourtDecission
    template_name = "archiv/courtdecission_detail.html"


class CourtDecissionCreate(CustomCreateView):
    h1 = "Create case"
    model = CourtDecission
    form_class = CourtDecissionForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CourtDecissionCreate, self).dispatch(*args, **kwargs)


class CourtDecissionUpdate(CustomUpdateView):
    h1 = "Edit case"
    model = CourtDecission
    form_class = CourtDecissionForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CourtDecissionUpdate, self).dispatch(*args, **kwargs)


class CourtDecissionDelete(DeleteView):
    model = CourtDecission
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:courtdecission_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CourtDecissionDelete, self).dispatch(*args, **kwargs)


class KeyWordListView(CustomListView):
    model = KeyWord
    h1 = "Browse keywords"
    create_button_text = "Create new keyword"
    filter_class = KeyWordListFilter
    formhelper_class = KeyWordFilterFormHelper
    table_class = KeyWordTable
    init_columns = [
        "id",
        "name",
    ]
    enable_merge = True

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ["archiv/custom_list.html"]
        else:
            return ["archiv/keyword_public_list.html"]

    def get_paginate_by(self, queryset):
        if self.request.user.is_authenticated:
            return 50
        else:
            None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            pass
        else:
            properties = [
                "name",
                "id",
                "part_of__name",
                "part_of__id",
            ]
            data = self.model.objects.all().values_list(*properties)
            df = pd.DataFrame(data=data, columns=properties)
            data = {}
            for gr, ndf in df.groupby("part_of__name"):
                data[gr] = ndf.to_dict("records")
            context["grouped_items"] = data
        return context


class KeyWordDetailView(CustomDetailView):
    model = KeyWord
    template_name = "archiv/keyword_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.part_of:
            context[
                "cases"
            ] = self.object.rvn_courtdecission_keyword_keyword.all().distinct()
            return context
        else:
            children = self.object.rvn_keyword_part_of_keyword.all()
            cases = CourtDecission.objects.filter(keyword__in=children).distinct()
            context["cases"] = cases
            return context


class KeyWordCreate(CustomCreateView):
    h1 = "Create keyword"
    model = KeyWord
    form_class = KeyWordForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(KeyWordCreate, self).dispatch(*args, **kwargs)


class KeyWordUpdate(CustomUpdateView):
    h1 = "Edit keyword"
    model = KeyWord
    form_class = KeyWordForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(KeyWordUpdate, self).dispatch(*args, **kwargs)


class KeyWordDelete(DeleteView):
    model = KeyWord
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:keyword_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(KeyWordDelete, self).dispatch(*args, **kwargs)


class PartialLegalSystemListView(CustomListView):
    model = PartialLegalSystem
    h1 = "Browse legal systems"
    create_button_text = "Create new legal system"
    filter_class = PartialLegalSystemListFilter
    formhelper_class = PartialLegalSystemFilterFormHelper
    table_class = PartialLegalSystemTable
    init_columns = [
        "id",
        "name",
        "legacy_pk",
    ]
    enable_merge = True

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ["archiv/custom_list.html"]
        else:
            return ["archiv/legalsystem_public_list.html"]

    def get_paginate_by(self, queryset):
        if self.request.user.is_authenticated:
            return 50
        else:
            None


class PartialLegalSystemDetailView(CustomDetailView):
    model = PartialLegalSystem
    template_name = "archiv/legalsystem_detail.html"


class PartialLegalSystemCreate(CustomCreateView):
    h1 = "Create legal system"
    model = PartialLegalSystem
    form_class = PartialLegalSystemForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PartialLegalSystemCreate, self).dispatch(*args, **kwargs)


class PartialLegalSystemUpdate(CustomUpdateView):
    h1 = "Edit legal system"
    model = PartialLegalSystem
    form_class = PartialLegalSystemForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PartialLegalSystemUpdate, self).dispatch(*args, **kwargs)


class PartialLegalSystemDelete(DeleteView):
    model = PartialLegalSystem
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:partiallegalsystem_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PartialLegalSystemDelete, self).dispatch(*args, **kwargs)


class PersonListView(CustomListView):
    model = Person
    h1 = "Browse authors"
    create_button_text = "Create new author"
    filter_class = PersonListFilter
    formhelper_class = PersonFilterFormHelper
    table_class = PersonTable
    init_columns = [
        "id",
        "last_name",
    ]
    enable_merge = True

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ["archiv/custom_list.html"]
        else:
            return ["archiv/author_public_list.html"]

    def get_paginate_by(self, queryset):
        if self.request.user.is_authenticated:
            return 50
        else:
            None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            pass
        else:
            properties = [
                "last_name",
                "first_name",
                "id",
                "legal_system__name",
                "legal_system__id",
            ]
            data = self.model.objects.exclude(legal_system=None).values_list(
                *properties
            )
            df = pd.DataFrame(data=data, columns=properties)
            df["name"] = df.apply(
                lambda x: f'{x["last_name"]}, {x["first_name"]}', axis=1
            )
            data = {}
            for gr, ndf in df.groupby("legal_system__name"):
                data[gr] = ndf.to_dict("records")
            context["grouped_items"] = data
        return context


class PersonDetailView(CustomDetailView):
    model = Person
    template_name = "archiv/person_detail.html"


class PersonCreate(CustomCreateView):
    h1 = "Create author"
    model = Person
    form_class = PersonForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonCreate, self).dispatch(*args, **kwargs)


class PersonUpdate(CustomUpdateView):
    model = Person
    h1 = "Edit author"
    form_class = PersonForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonUpdate, self).dispatch(*args, **kwargs)


class PersonDelete(DeleteView):
    model = Person
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:person_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonDelete, self).dispatch(*args, **kwargs)


class YearBookListView(CustomListView):
    model = YearBook
    h1 = "Browse bibliographic items"
    create_button_text = "Create new bibliographic item"
    filter_class = YearBookListFilter
    formhelper_class = YearBookFilterFormHelper
    table_class = YearBookTable
    init_columns = [
        "id",
        "title",
    ]
    enable_merge = True

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ["archiv/custom_list.html"]
        else:
            return ["archiv/yearbook_public_list.html"]

    def get_paginate_by(self, queryset):
        if self.request.user.is_authenticated:
            return 50
        else:
            None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            pass
        else:
            properties = [
                "title",
                "id",
                "year",
                "part_of__title",
                "part_of__id",
                "part_of__year",
            ]
            data = (
                self.model.objects.filter(has_bibliographic_items=None)
                .exclude(part_of=None)
                .exclude(year=None)
                .values_list(*properties)
            )
            df = pd.DataFrame(data=data, columns=properties)
            data = {}
            for gr, ndf in df.groupby("part_of__title"):
                data[gr] = ndf.to_dict("records")
            context["grouped_items"] = data
        return context


class YearBookDetailView(CustomDetailView):
    model = YearBook
    template_name = "archiv/yearbook_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.part_of:
            context[
                "cases"
            ] = self.object.related_court_decission.all().distinct()
            return context
        else:
            children = self.object.has_bibliographic_items.all()
            cases = CourtDecission.objects.filter(year_book_title__in=children).distinct()
            context["cases"] = cases
            return context


class YearBookCreate(CustomCreateView):
    h1 = "Create bibliographic item"
    model = YearBook
    form_class = YearBookForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(YearBookCreate, self).dispatch(*args, **kwargs)


class YearBookUpdate(CustomUpdateView):
    h1 = "Edit bibliographic item"
    model = YearBook
    form_class = YearBookForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(YearBookUpdate, self).dispatch(*args, **kwargs)


class YearBookDelete(DeleteView):
    model = YearBook
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:yearbook_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(YearBookDelete, self).dispatch(*args, **kwargs)


class TagListView(CustomListView):
    model = Tag
    h1 = "Browse tags"
    create_button_text = "Create new tag"
    filter_class = TagListFilter
    formhelper_class = TagFilterFormHelper
    table_class = TagTable
    init_columns = [
        "id",
        "name",
    ]
    enable_merge = True


class TagDetailView(CustomDetailView):
    model = Tag
    template_name = "archiv/tag_detail.html"


class TagCreate(CustomCreateView):
    h1 = "Create tag"
    model = Tag
    form_class = TagForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TagCreate, self).dispatch(*args, **kwargs)


class TagUpdate(CustomUpdateView):
    h1 = "Edit tag"
    model = Tag
    form_class = TagForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TagUpdate, self).dispatch(*args, **kwargs)


class TagDelete(DeleteView):
    model = Tag
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:tag_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TagDelete, self).dispatch(*args, **kwargs)
