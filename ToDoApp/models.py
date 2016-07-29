from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ToDoList(models.Model):
    listName = models.TextField(max_length=30)
    listDesc = models.TextField(max_length=50)
    listDueDate = models.DateField()

    def __unicode__(self):
        return self.listName

class ToDoItem(models.Model):
    itemName = models.TextField(max_length=30)
    itemDesc = models.TextField(max_length=20)
    itemCompleted = models.BooleanField(default=False)
    listId = models.ForeignKey(ToDoList)

    def __unicode__(self):
        return self.itemName

