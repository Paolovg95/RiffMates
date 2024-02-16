from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime

# Create your views here.

# Render template w/ context via template
def home(request):
    return render(request, "base.html", {})
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
def login_required(request):
    login_content = f"""
        <h1>You need to log in first</h1>

            <p> <a href="/accounts/login/">Log in</a> </p>
    """
    data = {
        'login_content': login_content,
    }
    return render(request, "general.html", data)
