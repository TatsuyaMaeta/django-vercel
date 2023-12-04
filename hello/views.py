from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.


def index(request):
    hello = ["こんにちは", "hello", "ola", "ニーハオ"]
    return render(request, "hello/index.html", {"hello": hello})


def cat(request):
    cats = ["pome", "mike", "jaa"]
    return render(request, "hello/cat.html", {"cats": cats})
