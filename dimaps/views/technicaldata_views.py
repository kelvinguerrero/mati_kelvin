from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from dimaps.models import TechnicalData


class TechnicalDataView(object):
    model = TechnicalData

    def get_template_names(self):
        """Nest templates within technicaldata directory."""
        tpl = super(TechnicalDataView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'technicaldata'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class TechnicalDataDateView(TechnicalDataView):
    date_field = 'created_at'
    month_format = '%m'


class TechnicalDataBaseListView(TechnicalDataView):
    paginate_by = 10


class TechnicalDataArchiveIndexView(
    TechnicalDataDateView, TechnicalDataBaseListView, ArchiveIndexView):
    pass


class TechnicalDataCreateView(TechnicalDataView, CreateView):
    pass


class TechnicalDataDateDetailView(TechnicalDataDateView, DateDetailView):
    pass


class TechnicalDataDayArchiveView(
    TechnicalDataDateView, TechnicalDataBaseListView, DayArchiveView):
    pass


class TechnicalDataDeleteView(TechnicalDataView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('dimaps_technicaldata_list')


class TechnicalDataDetailView(TechnicalDataView, DetailView):
    pass


class TechnicalDataListView(TechnicalDataBaseListView, ListView):
    pass


class TechnicalDataMonthArchiveView(
    TechnicalDataDateView, TechnicalDataBaseListView, MonthArchiveView):
    pass


class TechnicalDataTodayArchiveView(
    TechnicalDataDateView, TechnicalDataBaseListView, TodayArchiveView):
    pass


class TechnicalDataUpdateView(TechnicalDataView, UpdateView):
    pass


class TechnicalDataWeekArchiveView(
    TechnicalDataDateView, TechnicalDataBaseListView, WeekArchiveView):
    pass


class TechnicalDataYearArchiveView(
    TechnicalDataDateView, TechnicalDataBaseListView, YearArchiveView):
    make_object_list = True



