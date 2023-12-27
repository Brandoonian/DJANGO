"""Here we will define the paths to the different views"""
from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),  # (Homepage, Index page, Name is "index")
    path("", views.home, name="home"),
    path("create/", views.create, name="create")
]



