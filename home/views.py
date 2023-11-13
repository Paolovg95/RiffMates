from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.

def view_credits(request):
    content = "Paolo & Nicky"
    return render(request, "credits.html", {"content": content})

def view_about(request):
    code = HttpResponse.status_code
    content = f"This is about view. Code: {code}"
    return HttpResponse(content,content_type="text/plain")
def view_version(request):
    code = HttpResponse.status_code
    version = JsonResponse({ "Version": "1.0.0","code": code})
    return HttpResponse(version, content_type='application/json.')
