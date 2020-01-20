import django_filters
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
import django_tables2 as tables
from django_filters.views import FilterView
from django_tables2 import SingleTableView, SingleTableMixin

from event.forms import EventCreateForm
from event.models import Event


class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['name', 'event_start', 'insu_rgst_start']


class EventTable(tables.Table):
    class Meta:
        model = Event
        template_name = "django_tables2/bootstrap4.html"
        fields = ("name", "event_start", "insu_rgst_start")


class EventListView(SingleTableMixin, FilterView):
    template_name = 'event/list.html'
    model = Event
    table_class = EventTable
    filterset_class = EventFilter


class EventCreateView(View):
    def get(self, request):
        # 이벤트 생성 폼
        form = EventCreateForm()
        template_name = 'event/create.html'
        context = {'form': form}
        return render(request, template_name=template_name, context=context)

    def post(self, request):
        # 이벤트 생성
        pass
