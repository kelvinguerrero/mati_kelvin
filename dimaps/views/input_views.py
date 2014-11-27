from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from dimaps.models import Input


class InputView(object):
    model = Input

    def get_template_names(self):
        """Nest templates within input directory."""
        tpl = super(InputView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'input'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class InputDateView(InputView):
    date_field = 'created_at'
    month_format = '%m'


class InputBaseListView(InputView):
    paginate_by = 10


class InputArchiveIndexView(
    InputDateView, InputBaseListView, ArchiveIndexView):
    pass


class InputCreateView(InputView, CreateView):
    pass


class InputDateDetailView(InputDateView, DateDetailView):
    pass


class InputDayArchiveView(
    InputDateView, InputBaseListView, DayArchiveView):
    pass


class InputDeleteView(InputView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('dimaps_input_list')


class InputDetailView(InputView, DetailView):
    pass


class InputListView(InputBaseListView, ListView):
    pass


class InputMonthArchiveView(
    InputDateView, InputBaseListView, MonthArchiveView):
    pass


class InputTodayArchiveView(
    InputDateView, InputBaseListView, TodayArchiveView):
    pass


class InputUpdateView(InputView, UpdateView):
    pass


class InputWeekArchiveView(
    InputDateView, InputBaseListView, WeekArchiveView):
    pass


class InputYearArchiveView(
    InputDateView, InputBaseListView, YearArchiveView):
    make_object_list = True



