from django.contrib import admin

from event.models import Event, EventAttendantThrough, Attendant


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Attendant)
class EventAdminAdmin(admin.ModelAdmin):
    pass
