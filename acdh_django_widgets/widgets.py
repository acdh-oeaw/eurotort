import django_filters
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class RangeSliderWidget(django_filters.widgets.RangeWidget):
    template_name = "acdh_django_widgets/range_slider_widget.html"

    class Media:
        css = {
            "all": (
                "https://cdnjs.cloudflare.com/ajax/libs/noUiSlider/15.7.1/nouislider.css",
            )
        }
        js = (
            "https://cdnjs.cloudflare.com/ajax/libs/noUiSlider/15.7.1/nouislider.min.js",
            "https://cdnjs.cloudflare.com/ajax/libs/wnumb/1.2.0/wNumb.min.js",
        )

    def render(self, name, value, attrs=None, renderer=None):
        if value[0] is None:
            value = [self.attrs.get("min", 0), self.attrs.get("max", 100)]
        context = {"name": name, "value": value, "attrs": self.attrs}
        rendered = render_to_string(self.template_name, context)
        return mark_safe(rendered)
