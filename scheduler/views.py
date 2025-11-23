from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Event
import calendar
from datetime import datetime, timedelta
from collections import defaultdict


class EventListView(ListView):
    model = Event
    template_name = 'scheduler/event_list.html'
    context_object_name = 'events'
    paginate_by = 10


class EventDetailView(DetailView):
    model = Event
    template_name = 'scheduler/event_detail.html'
    context_object_name = 'event'


class EventCreateView(CreateView):
    model = Event
    template_name = 'scheduler/event_form.html'
    fields = ['title', 'description', 'start_time', 'end_time', 'location']
    success_url = reverse_lazy('event_list')


class EventUpdateView(UpdateView):
    model = Event
    template_name = 'scheduler/event_form.html'
    fields = ['title', 'description', 'start_time', 'end_time', 'location']
    success_url = reverse_lazy('event_list')


class EventDeleteView(DeleteView):
    model = Event
    template_name = 'scheduler/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')


def calendar_view(request, year=None, month=None):
    """Display a monthly calendar view with events."""
    # Get current date or use provided year/month
    today = timezone.now()
    if year is None:
        year = today.year
    if month is None:
        month = today.month

    # Create a calendar object
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]

    # Calculate previous and next month
    if month == 1:
        prev_month, prev_year = 12, year - 1
    else:
        prev_month, prev_year = month - 1, year

    if month == 12:
        next_month, next_year = 1, year + 1
    else:
        next_month, next_year = month + 1, year

    # Get all events for this month (using timezone-aware datetimes)
    start_date = timezone.make_aware(datetime(year, month, 1))
    if month == 12:
        end_date = timezone.make_aware(datetime(year + 1, 1, 1))
    else:
        end_date = timezone.make_aware(datetime(year, month + 1, 1))

    events = Event.objects.filter(
        start_time__gte=start_date,
        start_time__lt=end_date
    )

    # Group events by day
    events_by_day = defaultdict(list)
    for event in events:
        day = event.start_time.day
        events_by_day[day].append(event)

    context = {
        'calendar': cal,
        'month': month,
        'month_name': month_name,
        'year': year,
        'prev_month': prev_month,
        'prev_year': prev_year,
        'next_month': next_month,
        'next_year': next_year,
        'events_by_day': dict(events_by_day),
        'today': today,
    }

    return render(request, 'scheduler/calendar.html', context)
