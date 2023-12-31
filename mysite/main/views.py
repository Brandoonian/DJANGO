"""This file will store different views which can be thought of as like a webpage.
This is where we will write code that will serve http requests and show things on website"""
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

def index(response, id, name):
    ls = ToDoList.objects.get(id=id)
    print(name)
    return HttpResponse(f"<h1>{ls.name}</h1> <h2>{name}</h2>")


