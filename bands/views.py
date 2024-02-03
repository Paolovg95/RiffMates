from django.shortcuts import render, get_object_or_404
from bands.models import Musician, Band, Venue
from django.core.paginator import Paginator
# Create your views here.

def get_musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id )
    data = {
        'musician': musician,
        'bands': musician.band_set.all()
    }
    return render(request, "musician.html", data)

def get_musicians(request):
    musicians = Musician.objects.all().order_by("last_name")
    paginator = Paginator(musicians, 3)
    # Fetch the page key from the GET dictionary, defaulting to 1 if the key does not exist
    page_num = request.GET.get('page', 1)
    page_num  = int(page_num) # URLs are text, convert any value to an integer

    if page_num < 1: # Min value for 'page' = 1
        page_num = 1
    elif page_num > paginator.num_pages:
        page_num = paginator.num_pages

    page = paginator.page(page_num) # Returns a Page object with the given page_num based index


    musicians_bands = {}
    for musician in musicians:
        musicians_bands[musician.first_name + " " + musician.last_name] = len(musician.band_set.all())

    # Sort musicians in ascending order, result is a List of Tuples
    sorted_musicians_bands = sorted(musicians_bands.items(), key=lambda x:x[1], reverse=True)

    data = {
        'musicians': page.object_list, # list of objects in as 'musicians'
        'page': page, # page object,
        'sorted_musicians_bands': sorted_musicians_bands
    }
    return render(request, "musicians.html", data)

def get_band(request, band_id):
    band = Band.objects.get(id=band_id)
    data = {
        'band': band,
        'musicians': band.musicians.all()
    }
    return render(request, 'band.html', data)
def get_bands(request):
    bands = Band.objects.all()
    data = {
        'bands': bands
    }
    return render(request, "bands.html", data)

def get_venues(request):
    venues = Venue.objects.all().order_by("name")
    data = {
        'venues': venues
    }
    return render(request, "venues.html", data)
