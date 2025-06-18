from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ToDoList, Item 


# Create your views here.

def index(request, name):
    ls = ToDoList.objects.get(name=name)
    items = ls.item_set.all()

    # Build item list with status
    item_texts = ""
    for item in items:
        status = "✅" if item.complete else "❌"
        item_texts += f"{status} {item.text}<br>"

    return HttpResponse(f"<h1>{ls.name}</h1><br><br><h3>{item_texts}</h3>")



