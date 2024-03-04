# RiffMates/bands/api.py
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.text import slugify

from ninja import Router, ModelSchema

from bands.models import Venue

router = Router()

class VenueOut(ModelSchema):
    slug: str
    url: str

    class Meta:
        model = Venue
        fields = ["id", "name", "description"]

    # Ninja uses .resolve_X() static methods to populate the corresponding field.
    @staticmethod
    def resolve_slug(obj):
        slug = slugify(obj.name) + "-" + str(obj.id)
        return slug

    # The .resolve_url() method looks up the API end-point named fetch_venue and returns the corresponding URL
    @staticmethod
    def resolve_url(obj):
        url = reverse("api-1.0.0:fetch_url", args=[obj.id, ])
        return url

@router.get("/venue/{venue_id}/",
    response=VenueOut,
    url_name="fetch_url")
# The url_name argument to a Ninja decorator declares a name for the endpoint that can be looked up with a call to reverse()
def fetch_venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    return venue
