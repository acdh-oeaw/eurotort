# generated by appcreator
from crispy_bootstrap5.bootstrap5 import BS5Accordion
from crispy_forms.bootstrap import AccordionGroup
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit
from dal import autocomplete
from django import forms

from .models import Court
from .models import CourtDecission
from .models import KeyWord
from .models import PartialLegalSystem
from .models import Person
from .models import Tag
from .models import YearBook


class YearBookFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(YearBookFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Basic Search", "title", "part_of", "year", css_id="more"
                ),
                AccordionGroup("admin", "id", css_id="admin_search"),
            )
        )


class YearBookForm(forms.ModelForm):
    class Meta:
        model = YearBook
        exclude = ["legacy_id", "legacy_pk", "orig_data_csv"]
        widgets = {
            "part_of": autocomplete.ModelSelect2(url="archiv-ac:monograph-autocomplete")
        }

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
                    "partial_legal_system",
                    css_id="more",
                ),
                AccordionGroup("admin", "legacy_id", css_id="admin_search"),
            )
        )


class CourtForm(forms.ModelForm):
    class Meta:
        model = Court
        exclude = ["legacy_id", "legacy_pk", "orig_data_csv"]

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
                    "partial_legal_system",
                    "court",
                    "year_book_title",
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
            "legacy_id",
            "legacy_pk",
            "orig_data_csv",
            "full_text",
        ]
        widgets = {
            "tag": autocomplete.ModelSelect2Multiple(url="archiv-ac:tag-autocomplete"),
            "related_decision": autocomplete.ModelSelect2Multiple(
                url="archiv-ac:courtdecission-autocomplete"
            ),
            "author": autocomplete.ModelSelect2Multiple(
                url="archiv-ac:person-autocomplete"
            ),
            "keyword": autocomplete.ModelSelect2Multiple(
                url="archiv-ac:keyword-autocomplete"
            ),
            "year_book_title": autocomplete.ModelSelect2(
                url="archiv-ac:yearbook-autocomplete"
            ),
            "partial_legal_system": autocomplete.ModelSelect2(
                url="archiv-ac:partiallegalsystem-autocomplete"
            ),
            "court": autocomplete.ModelSelect2(url="archiv-ac:court-autocomplete"),
        }

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
        exclude = ["legacy_id", "legacy_pk", "orig_data_csv"]

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
                    "name",
                    css_id="more",
                ),
                AccordionGroup("admin", "legacy_id", css_id="admin_search"),
            )
        )


class PartialLegalSystemForm(forms.ModelForm):
    class Meta:
        model = PartialLegalSystem
        exclude = ["legacy_id", "legacy_pk", "orig_data_csv"]

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
                    css_id="more",
                ),
                AccordionGroup("admin", "legacy_id", css_id="admin_search"),
            )
        )


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ["legacy_id", "legacy_pk", "orig_data_csv"]

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


class TagFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(TagFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Basic Search",
                    "id",
                    "tag",
                    "last_name",
                    "first_name",
                    css_id="more",
                ),
            )
        )


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        exclude = ["legacy_id", "legacy_pk", "orig_data_csv"]

    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )
