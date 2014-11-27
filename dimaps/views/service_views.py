from django.shortcuts import render_to_response, render
from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from dimaps.models import Service
from django.db.models import Q


class ServiceView(object):
    model = Service

    def get_template_names(self):
        """Nest templates within service directory."""
        tpl = super(ServiceView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'service'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class ServiceDateView(ServiceView):
    date_field = 'created_at'
    month_format = '%m'


class ServiceBaseListView(ServiceView):
    paginate_by = 10


class ServiceArchiveIndexView(ServiceDateView, ServiceBaseListView, ArchiveIndexView):
    pass


class ServiceCreateView(ServiceView, CreateView):
    pass


class ServiceDateDetailView(ServiceDateView, DateDetailView):
    pass


class ServiceDayArchiveView(ServiceDateView, ServiceBaseListView, DayArchiveView):
    pass


class ServiceDeleteView(ServiceView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('dimaps_service_list')


class ServiceDetailView(ServiceView, DetailView):
    pass


class ServiceListView(ServiceBaseListView, ListView):
    pass


class ServiceSearchCategoryView(ServiceView, ListView):
    def get(self, request):
        search_text = request.GET.get('query', '')
        services = Service.objects.filter(Q(category__contains=search_text))
        return render(request, 'dimaps/service/service_search.html', {'services': services})


class ServiceSearchView(ServiceView, ListView):
    def get(self, request):
        search_text = request.GET.get('query', '')
        services = Service.objects.filter(Q(name__contains=search_text) |
                                          Q(description__contains=search_text) |
                                          Q(discovery_method__contains=search_text) |
                                          Q(business_function__contains=search_text) |
                                          Q(service_providers__contains=search_text) |
                                          Q(security__contains=search_text)
                                          )
        return render(request, 'dimaps/service/service_search.html', {'services': services})


class ServiceMonthArchiveView(ServiceDateView, ServiceBaseListView, MonthArchiveView):
    pass


class ServiceTodayArchiveView(ServiceDateView, ServiceBaseListView, TodayArchiveView):
    pass


class ServiceUpdateView(ServiceView, UpdateView):
    pass


class ServiceWeekArchiveView(ServiceDateView, ServiceBaseListView, WeekArchiveView):
    pass


class ServiceYearArchiveView(ServiceDateView, ServiceBaseListView, YearArchiveView):
    make_object_list = True



