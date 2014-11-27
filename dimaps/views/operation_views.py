from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from dimaps.models import Operation


class OperationView(object):
    model = Operation

    def get_template_names(self):
        """Nest templates within operation directory."""
        tpl = super(OperationView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'operation'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class OperationDateView(OperationView):
    date_field = 'created_at'
    month_format = '%m'


class OperationBaseListView(OperationView):
    paginate_by = 10


class OperationArchiveIndexView(
    OperationDateView, OperationBaseListView, ArchiveIndexView):
    pass


class OperationCreateView(OperationView, CreateView):
    pass


class OperationDateDetailView(OperationDateView, DateDetailView):
    pass


class OperationDayArchiveView(
    OperationDateView, OperationBaseListView, DayArchiveView):
    pass


class OperationDeleteView(OperationView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('dimaps_operation_list')


class OperationDetailView(OperationView, DetailView):
    pass


class OperationListView(OperationBaseListView, ListView):
    pass


class OperationMonthArchiveView(
    OperationDateView, OperationBaseListView, MonthArchiveView):
    pass


class OperationTodayArchiveView(
    OperationDateView, OperationBaseListView, TodayArchiveView):
    pass


class OperationUpdateView(OperationView, UpdateView):
    pass


class OperationWeekArchiveView(
    OperationDateView, OperationBaseListView, WeekArchiveView):
    pass


class OperationYearArchiveView(
    OperationDateView, OperationBaseListView, YearArchiveView):
    make_object_list = True



