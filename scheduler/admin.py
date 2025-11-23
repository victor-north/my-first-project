from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'location')
    list_filter = ('start_time', 'location')
    search_fields = ('title', 'description', 'location')
    ordering = ('start_time',)
    date_hierarchy = 'start_time'
