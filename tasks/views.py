import datetime

from django.http import HttpResponse
from django.shortcuts import render

def index(request, name):
    now = datetime.datetime.now()
    return render(request, "tasks/index.html", {
        "name": name.capitalize(),
        "day": now.day,
        "month": now.strftime("%B"),
        "year": now.year
    })

def greet(request, name):
    return HttpResponse(f"Ola, {name.capitalize()}")