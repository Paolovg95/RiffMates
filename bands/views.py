from django.shortcuts import render, get_object_or_404, redirect
from bands.models import Musician, Band, Venue, UserProfile
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models.signals import post_save
from bands.forms import VenueForm
from django.dispatch import receiver
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
    for venue in venues:
        # Mark the venue is "controlled" if the logged in user is
        # associated with the venue
        profile = request.user.userprofile
        venue.owned = \
            profile.venue_profiles.filter(\
            id=venue.id).exists()
    data = {
        'venue_owned': venue.owned,
        'venues': venues
    }
    return render(request, "venues.html", data)

# The musician_restricted view takes a Musician object ID as a parameter and checks if the authenticated user is either that musician or one of their bandmates.
def venues_restricted(user):
    try:
        user = user.userprofile
        return user.venue_profiles.all().exists
    except:
        redirect("/login/")

# If user.userprofile not exists = Not logged in
@user_passes_test(venues_restricted)
def venues_restricted(request):
    user_profile = request.user.userprofile
    venues = user_profile.venue_profiles.all()
    if not venues:
        content = f"""
            <h1>No venues associated to your profile</h1>

            <p>Move on</p>
        """
    else:
        content = f"""
            <h1>Venues associated:</h1>
        """
    context = {
        'venues': venues,
        'content': content,
    }
    return render(request, "general.html", context)

@login_required
def musicians_restricted(request):
    user_profile = request.user.userprofile
    musician = Musician.objects.get(userprofile=user_profile)
    # request.user is the authenticated user, .userprofile is the reverse relationship to the UserProfile ORM model
    allowed = False # True if Auth succeeds

    data = {
        'content': '<h1>Musician Profiles</h1>',
        'band_mates': [] # This will have all the band mates from every musician's bands
    }
    # Check user musician profile
    if musician:
        data['musician_profile'] = musician
        allowed = True
        musician_profiles = set(user_profile.musician_profiles.all())
        if musician_profiles:
            for band in musician.band_set.all(): # Iterate through the bands of user's musician profile.
                band_musicians = band.musicians.exclude(id=musician.id) # Append band mates
                data['band_mates'].append(band_musicians.distinct())
    if not allowed:
        raise Http404("Musician profile not found")
    return render(request, "general.html", data)

# Register this function to be called when a User object emits the post_save signal
@receiver(post_save , sender=User)
def user_post_save(sender, **kwargs):
    # Only take action if the User object is new and not created by a fixture, raw is True if the save is from a fixture being loaded

    if kwargs['created'] and not kwargs['raw']:
        user = kwargs['instance'] # Instance contains the object created
        try:
            # Double check UserProfile doesn't exist already
            # (admin might create it before the signal fires)
            UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            # No UserProfile exists for this user, create one
            UserProfile.objects.create(user=user)

# @receiver(user_login_failed,sender=User)
# def user_login_failed_view(sender, **kwargs):

@login_required()
def edit_venues(request, venue_id=0):

    if venue_id != 0:
        venue = get_object_or_404(Venue, id=venue_id)
        if not request.user.userprofile.venue_profiles.filter(id=venue_id).exists():
            raise Http404("Can't edit venues you don't own.")

    if request.method == 'GET': #GET
        if venue_id == 0:
            form = VenueForm()
        else:
            form = VenueForm(instance=venue)
    else: #POST
        # In the "add" case, create a new, empty Venue object to associate with the form
        if venue_id == 0:
            form = Venue.objects.create()

        form = VenueForm(request.POST, request.FILES, instance=venue)

        if form.is_valid():
            venue = form.save()
            # Add the (possibly new) venue to the user’s venues_controlled relationship. The .add() method handles the case where the relationship already exists.
            request.user.userprofile.venue_profiles.add(venue)
            redirect("/restricted_venues/")
    data = {
        'form': form
    }
    return render(request, 'edit_venue.html', data)
