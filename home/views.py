from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime

# Create your views here.

# Render template w/ context via template
def view_credits(request):

    credit_context = {
        "credit_names": ['Christopher', 'Lane', 'Paolo'],
        "page_name": "Credits"
    }
    # context = {
    #     "object": credit_context
    # }

    return render(request, "credits.html", credit_context)

# Render Http Response
def view_about(request):
    code = HttpResponse.status_code
    content = f"This is about view. Code: {code}"
    return HttpResponse(content,content_type="text/plain")


def view_version(request):
    code = HttpResponse.status_code
    data = { "Version": "1.0.0","code": code}
    return JsonResponse(data)

def view_news(request):
    current_dateTime = datetime.now()
    data = {
        'news':[
            ("RiffMates now has a news page!",current_dateTime),
            ("RiffMates has its first web page", current_dateTime),
        ],
    }
    return render(request, "news.html", data)
def venue_restricted(request):
    content = f"""
            <h1>No venuew associated</h1>

            <p>Move on</p>
        """
    data = {
        'content': content
    }
    return render(request, "general.html", data)
