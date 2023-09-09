# generated by appcreator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .filters import (
    CountryListFilter,
    CourtListFilter,
    CourtDecissionListFilter,
    KeyWordListFilter,
    PartialLegalSystemListFilter,
    PersonListFilter,
    YearBookListFilter,
)
from .forms import (
    CountryForm,
    CountryFilterFormHelper,
    CourtForm,
    CourtFilterFormHelper,
    CourtDecissionForm,
    CourtDecissionFilterFormHelper,
    KeyWordForm,
    KeyWordFilterFormHelper,
    PartialLegalSystemForm,
    PartialLegalSystemFilterFormHelper,
    PersonForm,
    PersonFilterFormHelper,
    YearBookFilterFormHelper,
    YearBookForm,
)
from .tables import (
    CountryTable,
    CourtTable,
    CourtDecissionTable,
    KeyWordTable,
    PartialLegalSystemTable,
    PersonTable,
    YearBookTable,
)
from .models import (
    Country,
    Court,
    CourtDecission,
    KeyWord,
    PartialLegalSystem,
    Person,
    YearBook,
)
from browsing.browsing_utils import (
    GenericListView,
    BaseCreateView,
    BaseUpdateView,
    BaseDetailView,
)


class CountryListView(GenericListView):
    model = Country
    filter_class = CountryListFilter
    formhelper_class = CountryFilterFormHelper
    table_class = CountryTable
    init_columns = [
        "id",
        "name",
    ]
    enable_merge = True


class CountryDetailView(BaseDetailView):
    model = Country
    template_name = "archiv/country_detail.html"


class CountryCreate(BaseCreateView):
    model = Country
    form_class = CountryForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CountryCreate, self).dispatch(*args, **kwargs)


class CountryUpdate(BaseUpdateView):
    model = Country
    form_class = CountryForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CountryUpdate, self).dispatch(*args, **kwargs)


class CountryDelete(DeleteView):
    model = Country
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:country_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CountryDelete, self).dispatch(*args, **kwargs)


class CourtListView(GenericListView):
    model = Court
    filter_class = CourtListFilter
    formhelper_class = CourtFilterFormHelper
    table_class = CourtTable
    init_columns = [
        "id",
        "name",
    ]
    enable_merge = True


class CourtDetailView(BaseDetailView):
    model = Court
    template_name = "archiv/court_detail.html"


class CourtCreate(BaseCreateView):
    model = Court
    form_class = CourtForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CourtCreate, self).dispatch(*args, **kwargs)


class CourtUpdate(BaseUpdateView):
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


class CourtDecissionListView(GenericListView):
    model = CourtDecission
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


class CourtDecissionDetailView(BaseDetailView):
    model = CourtDecission
    template_name = "archiv/courtdecission_detail.html"


class CourtDecissionCreate(BaseCreateView):
    model = CourtDecission
    form_class = CourtDecissionForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CourtDecissionCreate, self).dispatch(*args, **kwargs)


class CourtDecissionUpdate(BaseUpdateView):
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


class KeyWordListView(GenericListView):
    model = KeyWord
    filter_class = KeyWordListFilter
    formhelper_class = KeyWordFilterFormHelper
    table_class = KeyWordTable
    init_columns = [
        "id",
        "name",
    ]
    enable_merge = True


class KeyWordDetailView(BaseDetailView):
    model = KeyWord
    template_name = "archiv/keyword_detail.html"


class KeyWordCreate(BaseCreateView):
    model = KeyWord
    form_class = KeyWordForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(KeyWordCreate, self).dispatch(*args, **kwargs)


class KeyWordUpdate(BaseUpdateView):
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


class PartialLegalSystemListView(GenericListView):
    model = PartialLegalSystem
    filter_class = PartialLegalSystemListFilter
    formhelper_class = PartialLegalSystemFilterFormHelper
    table_class = PartialLegalSystemTable
    init_columns = [
        "id",
        "legacy_pk",
    ]
    enable_merge = True


class PartialLegalSystemDetailView(BaseDetailView):
    model = PartialLegalSystem
    template_name = "archiv/legalsystem_detail.html"


class PartialLegalSystemCreate(BaseCreateView):
    model = PartialLegalSystem
    form_class = PartialLegalSystemForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PartialLegalSystemCreate, self).dispatch(*args, **kwargs)


class PartialLegalSystemUpdate(BaseUpdateView):
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


class PersonListView(GenericListView):
    model = Person
    filter_class = PersonListFilter
    formhelper_class = PersonFilterFormHelper
    table_class = PersonTable
    init_columns = [
        "id",
        "last_name",
    ]
    enable_merge = True


class PersonDetailView(BaseDetailView):
    model = Person
    template_name = "archiv/person_detail.html"


class PersonCreate(BaseCreateView):
    model = Person
    form_class = PersonForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonCreate, self).dispatch(*args, **kwargs)


class PersonUpdate(BaseUpdateView):
    model = Person
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


class YearBookListView(GenericListView):
    model = YearBook
    filter_class = YearBookListFilter
    formhelper_class = YearBookFilterFormHelper
    table_class = YearBookTable
    init_columns = [
        "id",
        "title",
    ]
    enable_merge = True


class YearBookDetailView(BaseDetailView):
    model = YearBook
    template_name = "archiv/yearbook_detail.html"


class YearBookCreate(BaseCreateView):
    model = YearBook
    form_class = YearBookForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(YearBookCreate, self).dispatch(*args, **kwargs)


class YearBookUpdate(BaseUpdateView):
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
