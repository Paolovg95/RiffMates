from django.shortcuts import render, redirect
from .forms import CommentForm
from content.forms import CommentForm, SeekingAdForm
from django.core.mail import send_mail
from .models import SeekingAd, SeekingChoice
from django.contrib.auth.decorators import login_required

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
            return redirect("comment_accepted")
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



@login_required
def seeking_ad(request):
    if request.method == 'GET':
        form = SeekingAdForm()

    else: # POST
        form = SeekingAdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.owner = request.user
            ad.save()

            return redirect("ads")

    # Was a GET, or Form was not valid
    data = {
        "form": form,
    }

    return render(request, "seeking_ad.html", data)
