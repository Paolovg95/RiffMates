from django.contrib import admin
from django.utils.html import format_html
from bands.models import Musician, Venue, Room, Band
# Register your models here.
admin.site.register(Room)
admin.site.register(Venue)


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'id')
    search_fields = ('first_name', 'last_name',)

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
