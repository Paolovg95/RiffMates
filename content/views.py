from django.shortcuts import render, redirect
from .forms import CommentForm
from content.forms import CommentForm, SeekingAdForm
from django.core.mail import send_mail
from .models import SeekingAd, SeekingChoice

def comment_accepted(request):
    data = {
        "content": """
            <h1> Comment Accepted </h1>

            <p> Thanks for submitting a comment to <i>RiffMates</i> </p>
        """
    }

    return render(request, "general.html", data)

def comment(request):
    if request.method == 'GET':
        form = CommentForm()

    else: # POST
        form = CommentForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            comment = form.cleaned_data["comment"]

            message = f"""\
                Received comment from {name}\n\n
                {comment}
            """

            send_mail("Received comment", message,
                "admin@example.com", ["admin@example.com"],
                fail_silently=False)
            return redirect("/content/comment_accepted/")
    # Was a GET, or Form was not valid
    data = {
        "form": form,
    }
    return render(request, "comment.html", data)
# RiffMates/content/views.py

def list_ads(request):
    data = {
        'seeking_musician':SeekingAd.objects.filter(
            seeking=SeekingChoice.MUSICIAN),
        'seeking_band':SeekingAd.objects.filter(
            seeking=SeekingChoice.BAND),
    }
    return render(request, "list_ads.html", data)
