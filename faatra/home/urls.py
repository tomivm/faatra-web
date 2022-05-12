from django.urls import path

from . import views

urlpatterns = [
    path("about", views.who_we_are, name="who-we-are"),
    path("", views.index, name="index"),
]
