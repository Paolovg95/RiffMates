from django.shortcuts import render

# Create your views here.

def view_credits(request):
    content = "Paolo & Nicky"
    return render(request, "credits.html", {"content": content})
