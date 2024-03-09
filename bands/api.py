# RiffMates/bands/api.py
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.text import slugify
from typing import Optional
from ninja import Router, ModelSchema, Field, FilterSchema, Query

from bands.models import Venue, Room
from .auth_api import api_key

router = Router()

class VenueFilter(FilterSchema):
    name: Optional[str] = Field(None, q=["name__icontains"])

class RoomSchema(ModelSchema):
    class Meta:
        model = Room
        fields = ["id", "room_name"]

class VenueInSchema(ModelSchema):
    class Meta:
        model = Venue
        fields = ["name", "description"]

class VenueOutSchema(ModelSchema):
    slug: str
    url: str
    rooms: list[RoomSchema] = Field(None, alias="room_set") # Field class allows you to rename it from room_set

    # To nest the room data, use a list of RoomSchema type hint, which when combined with the Field class allows you to rename it from room_set

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
        # The url_name argument to a Ninja decorator declares a name for the endpoint that can be looked up with a call to reverse()
        url = reverse("api-1.0.0:fetch_url", args=[obj.id, ])
        return url



# GET Venue
@router.get("/venue/{venue_id}/",
    response=VenueOutSchema,
    url_name="fetch_url")
def fetch_venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    return venue

# POST Venue
@router.post("/venue/", response=VenueOutSchema, auth=api_key)
def create_venue(request, payload:VenueInSchema):
    venue = Venue.objects.create(**payload.dict())
    return venue

# GET Venues
@router.get("/venues/", response=list[VenueOutSchema])
def fetch_name(request, filters: VenueFilter = Query(...)):
    venues = Venue.objects.all()
    venues = filters.filter(venues)
    return venues

    # The filters object is an instance of VenueFilter

    # .filter() which takes a QuerySet (venues) and filters it based on the instantiated values of the FilterSchema object



# GET API Venue name
#Support a query parameter called "name" Ex: api/v1/bands/venues/?name=CBGB
# @router.get("/venues/", response=list[VenueOut])
# def fetch_venues(request, name=None):
#     venues = Venue.objects.all()
#     if name != None:
#         venues = venues.filter(name__istartswith=name)
#     return venues
