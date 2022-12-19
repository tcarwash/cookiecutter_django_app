from django.shortcuts import render
from django.contrib import messages


# Create your views here.
def home(request):
    context = {"title": "Home"}
    return render(
        request, "{{ cookiecutter.appname }}/{{ cookiecutter.appname }}.html", context
    )


def about(request):
    context = {"title": "About"}
    return render(
        request,
        "{{ cookiecutter.appname }}/{{ cookiecutter.appname }}_about.html",
        context,
    )
