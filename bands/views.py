from django.shortcuts import render, get_object_or_404, redirect
from bands.models import Musician, Band, Venue, UserProfile
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_login_failed
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
    data = {
        'venues': venues
    }
    return render(request, "venues.html", data)

# The musician_restricted view takes a Musician object ID as a parameter and checks if the authenticated user is either that musician or one of their bandmates.
def venues_restricted(user):
    try:
        user = user.userprofile
        return user.venue_profiles.all().exists
    except:
        redirect("/restricted/") # If user.userprofile not exists = Not logged in

@user_passes_test(venues_restricted, login_url="/restricted/")
def venues_restricted(request):
    user_profile = request.user.userprofile
    venues = user_profile.venue_profiles.all()
    if venues:
        content = f"""
            <h1>Venues associated:
                <br>{venues.first()}
            </h1>

            <p> <a href="/accounts/logout/">Logout</a> </p>
        """
    else:
        content = f"""
            <h1>No venues associated</h1>

            <p>Move on</p>
        """
    context = {
        'venues': venues,
        'content': content,
    }
    return render(request, "general.html", context)



@login_required
def musician_restricted(request, musician_id):
    musician = Musician.objects.get(id=musician_id)
    # request.user is the authenticated user, .userprofile is the reverse relationship to the UserProfile ORM model
    user_profile = request.user.userprofile
    allowed = False # True if Auth succeeds

    # Check
    if user_profile.musician_profiles.filter(id=musician_id).exists():
        allowed = True
        content = f"""
            <h1>Your musician profile: {musician.first_name} {musician.last_name}</h1>

            <p> <a href="/accounts/logout/">Logout</a> </p>
        """
    else:
        musician_profiles = set(user_profile.musician_profiles.all())
        for band in musician.band_set.all():
            band_musicians = set(band.musicians.all())
            if musician_profiles.intersection(band_musicians):
                allowed = True
                content = f"""
                    <h1>Band member profile: {musician.first_name} {musician.last_name}</h1>
                    <h2>From {band.name}</h2>

                    <p> <a href="/accounts/logout/">Logout</a> </p>
                """
            break
    # If User is not this musician, check if they're a band-mate
    if not allowed:
        raise Http404("Musician profile not found")
    data = {
        'title': 'Musician Restricted',
        'content': content,
    }

    return render(request, "general.html", data)

# Register this function to be called when a User object emits the post_save signal
@receiver(post_save, sender=User)
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
