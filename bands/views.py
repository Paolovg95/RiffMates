from django.shortcuts import render
from django.shortcuts import get_object_or_404
from bands.models import Musician
# Create your views here.

def get_musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id )
    data = {
        'musician': musician
    }
    return render(request, "musician.html", data)