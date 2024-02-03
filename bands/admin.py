from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import User
from bands.models import Musician, Venue, Room, Band, UserProfile
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


class UserProfileInline(admin.StackedInline): # Create a form by inheriting from admin.StackedInline
    model = UserProfile
    can_delete = False

class UserAdmin(admin.ModelAdmin): # Create a new object to admin the User model, inheriting from the original
    inlines = [UserProfileInline]
# Use the new UserProfileInline class as a stacked-form

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
