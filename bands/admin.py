from django.contrib import admin
from bands.models import Musician, Venue, Room, Band
# Register your models here.
admin.site.register(Room)
admin.site.register(Venue)

class MusicianAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','last_name')
    search_fields = ('first_name', 'last_name',)
admin.site.register(Musician, MusicianAdmin)

class BandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(Band,BandAdmin)
