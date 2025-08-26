from django.contrib import admin
from .models import Event  # Import your model

# Register the Event model with admin
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('name', 'date', 'location', 'description')

    # Fields to filter by in the admin interface
    list_filter = ('date', 'location')

    # Fields to search in the admin interface
    search_fields = ('name', 'description')
