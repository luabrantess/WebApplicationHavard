import datetime

from django import forms
from django.http import HttpResponse
from django.shortcuts import render

tasks = []

class NewTask(forms.Form):
    task = forms.CharField(label="New task")

def index(request, name):
    now = datetime.datetime.now()

    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request, "tasks/index.html", {
                "form": form
            })

    return render(request, "tasks/index.html", {
        "name": name.capitalize(),
        "day": now.day,
        "month": now.strftime("%B"),
        "year": now.year,
        "form": NewTask(),
        "tasks": tasks

    })


