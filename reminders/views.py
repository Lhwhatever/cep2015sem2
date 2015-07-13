from django.shortcuts import render
from django.http import HttpResponse
from reminders import models

# Create your views here.
def index(request, *args):
    return render(request, "task_index.html", {'tasks': models.Task.objects.all()})
    
def task_detail(request, task_id):
    try:
        task = models.Task.objects.get(id=task_id)
        return render(request, "task.html", {'task': task})
    except models.Task.DoesNotExist:
        return render(request, "task.html", {'task': None})