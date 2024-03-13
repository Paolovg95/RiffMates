from django.shortcuts import render
from .models import Promoter

from time import sleep

def partial_promoters(request):
    sleep(2)
    data = {
        "promoters": Promoter.objects.all(),
    }
    return render(request, "partials/promoters.html", data)

def promoters(request):
    return render(request, "promoters.html")
