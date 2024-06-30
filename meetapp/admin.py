from django.contrib import admin
from .models import Meet, Participant

@admin.register(Meet)
class MeetAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_datetime', 'status', 'date_created', 'date_updated')
    list_filter = ('status', 'start_datetime')
    search_fields = ('name', 'description')
    readonly_fields = ('date_created', 'date_updated')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'image', 'start_datetime', 'status')
        }),
        ('Timestamps', {
            'fields': ('date_created', 'date_updated')
        }),
    )

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_registered')
    search_fields = ('first_name', 'last_name', 'email', 'description')
    readonly_fields = ('date_registered',)
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'description', 'meets')
        }),
        ('Registration Date', {
            'fields': ('date_registered',)
        }),
    )
