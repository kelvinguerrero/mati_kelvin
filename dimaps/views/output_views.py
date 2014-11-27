from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from dimaps.models import Output


class OutputView(object):
    model = Output

    def get_template_names(self):
        """Nest templates within output directory."""
        tpl = super(OutputView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'output'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class OutputDateView(OutputView):
    date_field = 'created_at'
    month_format = '%m'


class OutputBaseListView(OutputView):
    paginate_by = 10


class OutputArchiveIndexView(
    OutputDateView, OutputBaseListView, ArchiveIndexView):
    pass


class OutputCreateView(OutputView, CreateView):
    pass


class OutputDateDetailView(OutputDateView, DateDetailView):
    pass


class OutputDayArchiveView(
    OutputDateView, OutputBaseListView, DayArchiveView):
    pass


class OutputDeleteView(OutputView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('dimaps_output_list')


class OutputDetailView(OutputView, DetailView):
    pass


class OutputListView(OutputBaseListView, ListView):
    pass


class OutputMonthArchiveView(
    OutputDateView, OutputBaseListView, MonthArchiveView):
    pass


class OutputTodayArchiveView(
    OutputDateView, OutputBaseListView, TodayArchiveView):
    pass


class OutputUpdateView(OutputView, UpdateView):
    pass


class OutputWeekArchiveView(
    OutputDateView, OutputBaseListView, WeekArchiveView):
    pass


class OutputYearArchiveView(
    OutputDateView, OutputBaseListView, YearArchiveView):
    make_object_list = True



