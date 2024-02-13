from django.contrib import admin
from django.utils.text import Truncator

from content.models import SeekingAd


@admin.register(SeekingAd)
class SeekingAdAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "owner", "seeking", "show_ad", )

    def show_ad(self, obj):
        # Pass Truncator the ad’s content field restricting the result to 5 words long, appending " …" if content got truncated
        return Truncator(obj.content).words(5, truncate=' ...')
    show_ad.short_description = "Ad"
#The short_description attribute for the method changes the title in the Django Admin listing page
