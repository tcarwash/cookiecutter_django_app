from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="{{ cookiecutter.appname }}-home"),
    path("about/", views.about, name="{{ cookiecutter.appname }}-about"),
]
