from django.shortcuts import render
from . import models

#home view:
def index(request):
    todos = models.Todo.objects.all().order_by('-id')
    return render(request, 'index.html', {'todos': todos})

def create_todo(request):
    title = request.POST.get('title')
    todo = models.Todo.objects.create(title=title)
    todo.save()
    todos = models.Todo.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})

def mark_todo(request, pk):
    todo = models.Todo.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    todos = models.Todo.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})

def delete_todo(request, pk):
    todo = models.Todo.objects.get(pk=pk)
    todo.delete()
    todos = models.Todo.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})
