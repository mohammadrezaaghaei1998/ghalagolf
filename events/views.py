from django.shortcuts import render
from .models import CalendarEvent


# Create your views here.

# def calender(request):    
#     return render(request, 'calender.html')


def calendar(request):
    events = CalendarEvent.objects.all()

    event_data = {}
    for ev in events:
        if ev.month not in event_data:
            event_data[ev.month] = {}
        if ev.day not in event_data[ev.month]:
            event_data[ev.month][ev.day] = []
        event_data[ev.month][ev.day].append(ev)

    return render(request, 'calender.html', {
        "events": events,
        "event_data": event_data,
    })
