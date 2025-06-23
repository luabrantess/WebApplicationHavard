import datetime

from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from .models import Tasks


class NewTask(forms.Form):
    task = forms.CharField(label="New task")

def index(request, name):
    now = datetime.datetime.now()

    if "tasks" not in request.session:
        request.session["tasks"] = []

    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
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
        "tasks": Tasks.objects.all()

    })

def task(request, tasks_id):
    task = Tasks.objects.get(id=tasks_id)
    return render(request, "tasks/task.html")
