from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item 
from .forms import CreateNewList 

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id) 

    if response.method == "POST":
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = False
                else:
                    item.complete = True
                item.save()


        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete= False)
            else:
                print("Invalid")
    

    return render(response, "myapp/list.html", {"ls": ls})

def home(response):
    return render(response, "myapp/home.html", {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "myapp/create.html", {"form":form})

def view(response):
    return render(response, "myapp/view.html", {})
