from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Event


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
