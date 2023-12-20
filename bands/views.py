from django.shortcuts import render, get_object_or_404
from bands.models import Musician
from django.core.paginator import Paginator
# Create your views here.

def get_musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id )
    data = {
        'musician': musician
    }
    return render(request, "musician.html", data)
def get_musicians(request):
    musicians = Musician.objects.all().order_by("last_name")
    paginator = Paginator(musicians, 3)
    # Fetch the page key from the GET dictionary, defaulting to 1 if the key does not exist
    page_num = request.GET.get('page')
    page_num  = int(page_num) # URLs are text, convert any value to an integer

    if page_num < 1: # Min value for 'page' = 1
        page_num = 1
    elif page_num > paginator.num_pages:
        page_num = paginator.num_pages

    page = paginator.page(page_num) # Fetch the page object containing the subset of items

    data = {
        'musicians': page.object_list, # list of objects in as 'musicians'
        'page': page
    }
    return render(request, "musicians.html", data)
