"""Here we will define the paths to the different views"""
from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>/<str:name>", views.index, name="index"),  # (Homepage, Index page, Name is "index"

]



