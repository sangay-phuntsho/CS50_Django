from django.urls import reverse
from http.client import HTTPResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
import hobbies
# Create your views here.

# Generate form elements
class NewHobbiesForm(forms.Form):
    hobby = forms.CharField(label="New Hobby:")

def index(request):
    if not "hobbies" in request.session:
        request.session["hobbies"] = []     
    return render(request, "hobbies/index.html", {
        "hobbies":request.session["hobbies"]
    })

def add(request):
    if request.method == "POST":
        form = NewHobbiesForm(request.POST)
        if form.is_valid():
            hobby = form.cleaned_data["hobby"]
            request.session["hobbies"] += [hobby]
            return HttpResponseRedirect(reverse("hobbies:index"))
        else:
            return render(request, "hobbies/add.html", {
                "form":form
            })
    return render(request, "hobbies/add.html", {
        "form": NewHobbiesForm()
    })      