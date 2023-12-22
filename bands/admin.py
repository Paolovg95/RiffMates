from django.contrib import admin
from bands.models import Musician, Venue, Room, Band
# Register your models here.
admin.site.register(Room)
admin.site.register(Venue)
admin.site.register(Band)

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','last_name')
