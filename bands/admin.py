from django.contrib import admin
from bands.models import Musician, Venue, Room
# Register your models here.
admin.site.register(Musician)
admin.site.register(Room)
admin.site.register(Venue)
