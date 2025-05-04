import datetime

from django.http import HttpResponse
from django.shortcuts import render

tasks = ["foo", "bar", "baz"]

def index(request, name):
    now = datetime.datetime.now()
    return render(request, "tasks/index.html", {
        "tasks": tasks,
        "name": name.capitalize(),
        "day": now.day,
        "month": now.strftime("%B"),
        "year": now.year
    })

