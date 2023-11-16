from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.

# Render template w/ context via template
def view_credits(request):

    credit_context = {
        "credit_names": ['Paolo', 'Nicky'],
        "page_name": "Credits page"
    }
    context = {
        "object": credit_context
    }

    return render(request, "credits.html", context)

# Render Http Response
def view_about(request):
    code = HttpResponse.status_code
    content = f"This is about view. Code: {code}"
    return HttpResponse(content,content_type="text/plain")


def view_version(request):
    code = HttpResponse.status_code
    data = { "Version": "1.0.0","code": code}
    return JsonResponse(data)
