from django.urls import path

from event.views import EventCreateView, EventListView

app_name = 'event'
urlpatterns = [
    path('', EventListView.as_view(), name='list'),
    path('create/', EventCreateView.as_view(), name='create'),
]
