# RiffMates/bands/api.py
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.text import slugify
from typing import Optional
from ninja import Router, ModelSchema, Field, FilterSchema, Query

from bands.models import Venue

router = Router()

class VenueFilter(FilterSchema):
    name: Optional[str] = None

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


# The url_name argument to a Ninja decorator declares a name for the endpoint that can be looked up with a call to reverse()

# GET API Venue id
@router.get("/venue/{venue_id}/",
    response=VenueOut,
    url_name="fetch_url")
def fetch_venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    return venue

# GET API Venue name
#Support a query parameter called "name" Ex: api/v1/bands/venues/?name=CBGB
# @router.get("/venues/", response=list[VenueOut])
# def fetch_venues(request, name=None):
#     venues = Venue.objects.all()
#     if name != None:
#         venues = venues.filter(name__istartswith=name)
#     return venues

@router.get("/venues/", response=list[VenueOut])
def fetch_name(request, filters: VenueFilter = Query(...)):
    venues = Venue.objects.all()
    venues = filters.filter(venues)
    return venues
