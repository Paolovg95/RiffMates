from django.shortcuts import render, get_object_or_404
from bands.models import Musician
# Create your views here.

def get_musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id )
    data = {
        'musician': musician
    }
    return render(request, "musician.html", data)
def get_musicians(request):
    musicians = Musician.objects.all()
    data = {
        'musicians': musicians.order_by("last_name")
    }
    return render(request, "musicians.html", data)
