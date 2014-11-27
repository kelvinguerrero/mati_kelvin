from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from dimaps.models import ServiceConsumer


class ServiceConsumerView(object):
    model = ServiceConsumer

    def get_template_names(self):
        """Nest templates within serviceconsumer directory."""
        tpl = super(ServiceConsumerView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'serviceconsumer'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class ServiceConsumerDateView(ServiceConsumerView):
    date_field = 'created_at'
    month_format = '%m'


class ServiceConsumerBaseListView(ServiceConsumerView):
    paginate_by = 10


class ServiceConsumerArchiveIndexView(
    ServiceConsumerDateView, ServiceConsumerBaseListView, ArchiveIndexView):
    pass


class ServiceConsumerCreateView(ServiceConsumerView, CreateView):
    pass


class ServiceConsumerDateDetailView(ServiceConsumerDateView, DateDetailView):
    pass


class ServiceConsumerDayArchiveView(
    ServiceConsumerDateView, ServiceConsumerBaseListView, DayArchiveView):
    pass


class ServiceConsumerDeleteView(ServiceConsumerView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('dimaps_serviceconsumer_list')


class ServiceConsumerDetailView(ServiceConsumerView, DetailView):
    pass


class ServiceConsumerListView(ServiceConsumerBaseListView, ListView):
    pass


class ServiceConsumerMonthArchiveView(
    ServiceConsumerDateView, ServiceConsumerBaseListView, MonthArchiveView):
    pass


class ServiceConsumerTodayArchiveView(
    ServiceConsumerDateView, ServiceConsumerBaseListView, TodayArchiveView):
    pass


class ServiceConsumerUpdateView(ServiceConsumerView, UpdateView):
    pass


class ServiceConsumerWeekArchiveView(
    ServiceConsumerDateView, ServiceConsumerBaseListView, WeekArchiveView):
    pass


class ServiceConsumerYearArchiveView(
    ServiceConsumerDateView, ServiceConsumerBaseListView, YearArchiveView):
    make_object_list = True



