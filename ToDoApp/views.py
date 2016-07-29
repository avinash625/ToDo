from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template

from ToDoApp.models import ToDoList, ToDoItem


def todolistView(request):
    todolists = ToDoList.objects.all()
    template = get_template("todolistView.html")
    result = template.render( context={"todolists": todolists })
    return HttpResponse(result)


def perListView(request,id):
    items = ToDoItem.objects.filter(listId__exact= id)
    template = get_template("perListView.html")
    result = template.render(context={"items": items})
    return HttpResponse(result)

