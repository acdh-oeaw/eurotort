import django_tables2

from django_tables2.export.views import ExportMixin

from . models import CourtDecission
from . tables import ResultsTable
from . filters import CourtDecissionFulltextFilter


class EventResultView(ExportMixin, django_tables2.SingleTableView):

    filter_class = CourtDecissionFulltextFilter
    model = CourtDecission
    context_filter_name = 'filter'
    paginate_by = 50
    template_name = 'archiv/event_result.html'
    table_class = ResultsTable

    def get_queryset(self, **kwargs):
        qs = super(EventResultView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        return self.filter.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super(EventResultView, self).get_context_data()
        context['query_string'] = self.request.GET.get('ft_search', None)
        return context
