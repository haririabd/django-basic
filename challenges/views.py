from calendar import month
from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "January is working!",
    "february": "February is working!",
    "march": "March is working!",
    "april": "April is working!",
    "may": "May is my birth month!",
    "june": "June is working!",
    "july": "July is working!",
    "august": "August is working!",
    "september": "September is working!",
    "october": "October is working!",
    "november": "November is working!",
    "december": "December is working!"
}

# This is a function
# 2nd parameter is month bcos we declare month in the <> at the path in urls file


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "month": months
    })


def monthly_challenge_by_number(request, month):
    # assign months as the list of keys from our dictionary.
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    # List items are indexed, so we can access each index below. so index 0 is january and so on
    redirect_month = months[month - 1]

    # The name month_challenge will construct our url based on rule in project urls file which is /challenges/
    # Then args will pass the number or index from our list making url /challenge/january
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    # try run the statement first, if no match, do the rest
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "months": month
        })

    except:
        raise Http404()
