# RiffMates/bands/api.py
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.text import slugify
from typing import Optional
from ninja import Router, ModelSchema, Field, FilterSchema, Query

from bands.models import Venue, Room, Musician, Band
from .auth_api import api_key

router = Router()

# ------------- MUSICIAN/BANDS schemas -------------
class MusicianSchema(ModelSchema):
    class Meta:
        model = Musician
        fields = ["first_name", "last_name"]
class MusicianInSchema(ModelSchema):
    class Meta:
        model = Musician
        fields = ["first_name"]
class BandOutSchema(ModelSchema):
    class Meta:
        model = Band
        fields = ["id", "name"]
    musicians: list[MusicianSchema]
class MusicianOutSchema(ModelSchema):
    bands: list[BandOutSchema] = Field(None, alias="band_set")
    class Meta:
        model = Musician
        fields = ["first_name", "last_name","birth_date"]


# ------------- VENUE/ROOMS schemas -------------
class VenueSchema(ModelSchema):
    class Meta:
        model = Venue
        fields = ["id", "name"]
class VenueFilter(FilterSchema):
    name: Optional[str] = Field(None, q=["name__icontains"])
class VenueInSchema(ModelSchema):
    class Meta:
        model = Venue
        fields = ["name", "description"]
class RoomOutSchema(ModelSchema):
    class Meta:
        model = Room
        fields = ["id", "room_name"]
class VenueOutSchema(ModelSchema):
    slug: str
    url: str
    rooms: list[RoomOutSchema] = Field(None, alias="room_set") # Field class allows you to rename it from room_set
    # To nest the room data, use a list of RoomOutSchema type hint, which when combined with the Field class allows you to rename it from room_set
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

# ------------- Endpoints -------------

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

# GET Room
@router.get("/room/{room_id}/", response=RoomOutSchema)
def fetch_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return room


# GET Musician
@router.get("/musician/{musician_id}/", response=MusicianOutSchema)
def fetch_musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    return musician

# GET Musicians
@router.get("/musicians/", response=list[MusicianOutSchema])
def fetch_musicians(request):
    musicians = Musician.objects.all()
    return musicians

# POST Musician
@router.post("/musician/", response=MusicianOutSchema, auth=api_key)
def create_musician(request, payload:MusicianInSchema):
    musician = Musician.objects.create(**payload.dict())
    return musician
# PUT Musician
@router.put("/musician/{musician_id}/", response=MusicianOutSchema, auth=api_key)
def update_musician(request, musician_id, payload:MusicianInSchema):
    musician = get_object_or_404(Musician, id=musician_id)
    for key, value in payload.dict().items():
        setattr(musician, key, value)
    musician.save()
    return musician

# GET Bands
@router.get("/bands/", response=list[BandOutSchema])
def fetch_bands(request):
    bands = Band.objects.all()
    return bands

# GET API Venue name
#Support a query parameter called "name" Ex: api/v1/bands/venues/?name=CBGB
# @router.get("/venues/", response=list[VenueOut])
# def fetch_venues(request, name=None):
#     venues = Venue.objects.all()
#     if name != None:
#         venues = venues.filter(name__istartswith=name)
#     return venues
