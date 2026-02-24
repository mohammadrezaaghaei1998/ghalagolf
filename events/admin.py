from django.contrib import admin
from .models import CalendarEvent,ScheduleYear

# Register your models here.


admin.site.register(CalendarEvent)
admin.site.register(ScheduleYear)
