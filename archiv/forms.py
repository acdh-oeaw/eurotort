# generated by appcreator
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import AccordionGroup
from crispy_bootstrap5.bootstrap5 import BS5Accordion

from .models import (
    Country,
    Court,
    CourtDecission,
    KeyWord,
    PartialLegalSystem,
    Person,
)


class CountryFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(CountryFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Advanced search", "id", "legacy_pk", "name", css_id="more"
                ),
                AccordionGroup("admin", "legacy_id", css_id="admin_search"),
            )
        )


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CountryForm, self).__init__(*args, **kwargs)
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
                    "Advanced search",
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
                    "Advanced search",
                    "id",
                    "legacy_pk",
                    "country",
                    "partial_legal_system",
                    "court",
                    "decission_date",
                    "file_number",
                    "party",
                    "location",
                    "yearbook",
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
        fields = "__all__"

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
                    "Advanced search",
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
                    "Advanced search",
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
                    "Advanced search",
                    "id",
                    "legacy_pk",
                    "last_name",
                    "first_name",
                    "cv",
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
