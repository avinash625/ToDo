from django.contrib.contenttypes import fields
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from ToDoApp.models import *

class ListCreateView(CreateView):
    model = ToDoList
    fields = ['listName','listDesc','listDueDate']
    template_name = "ToDoApp/ListCreateView.html"
    success_url = "/todo/lists"

class ListDeleteView(DeleteView):
    model = ToDoList
    fields = ['listName','listDesc','listDueDate']
    template_name = "ToDoApp/ListDeleteView.html"
    success_url = "/todo/lists"

class ListUpdateView(UpdateView):
    model = ToDoList
    fields = ['listName','listDesc','listDueDate']
    template_name = "ToDoApp/ListUpdateView.html"
    success_url = "/todo/lists"

class ListListView(ListView):
    model = ToDoList
    fields = ['listName','listDesc','listDueDate']

class ListDetailView(DetailView):
    model = ToDoList
