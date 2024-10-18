from django.urls import path

from . import views

urlpatterns = [
    path("TS1", views.index, name="index"),
]
