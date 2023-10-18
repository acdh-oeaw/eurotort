# generated by appcreator
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import AccordionGroup
from crispy_bootstrap5.bootstrap5 import BS5Accordion

from .models import (
    Court,
    CourtDecission,
    KeyWord,
    PartialLegalSystem,
    Person,
    YearBook,
)


class YearBookFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(YearBookFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup("Basic Search", "title", css_id="more"),
                AccordionGroup("admin", "id", css_id="admin_search"),
            )
        )


class YearBookForm(forms.ModelForm):
    class Meta:
        model = YearBook
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(YearBookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class CourtFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(CourtFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Basic Search",
                    "id",
                    "legacy_pk",
                    "name",
                    "abbreviation",
                    "is_high_court",
                    "country",
                    "partial_legal_system",
                    css_id="more",
                ),
                AccordionGroup("admin", "legacy_id", css_id="admin_search"),
            )
        )


class CourtForm(forms.ModelForm):
    class Meta:
        model = Court
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CourtForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class CourtDecissionFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(CourtDecissionFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Basic Search",
                    "id",
                    "ft_search",
                    "legacy_pk",
                    "country",
                    "partial_legal_system",
                    "court",
                    "year_book_title",
                    "decission_date",
                    "file_number",
                    "party",
                    "location",
                    "short_description",
                    "situation",
                    "motto",
                    "commentary",
                    "additional_information",
                    "keyword",
                    "author",
                    css_id="more",
                ),
                AccordionGroup("admin", "legacy_id", css_id="admin_search"),
            )
        )


class CourtDecissionForm(forms.ModelForm):
    class Meta:
        model = CourtDecission
        exclude = [
            "vector_column",
        ]

    def __init__(self, *args, **kwargs):
        super(CourtDecissionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class KeyWordFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(KeyWordFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Basic Search",
                    "id",
                    "legacy_pk",
                    "name",
                    "part_of",
                    css_id="more",
                ),
                AccordionGroup("admin", "legacy_id", css_id="admin_search"),
            )
        )


class KeyWordForm(forms.ModelForm):
    class Meta:
        model = KeyWord
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(KeyWordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class PartialLegalSystemFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PartialLegalSystemFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Basic Search",
                    "id",
                    "legacy_pk",
                    "country",
                    "name",
                    css_id="more",
                ),
                AccordionGroup("admin", "legacy_id", css_id="admin_search"),
            )
        )


class PartialLegalSystemForm(forms.ModelForm):
    class Meta:
        model = PartialLegalSystem
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PartialLegalSystemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class PersonFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PersonFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Basic Search",
                    "id",
                    "legacy_pk",
                    "last_name",
                    "first_name",
                    "nationality",
                    css_id="more",
                ),
                AccordionGroup("admin", "legacy_id", css_id="admin_search"),
            )
        )


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )
