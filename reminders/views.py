from django.shortcuts import render
from django.http import HttpResponse
from reminders import models

# Create your views here.
def index(request):
    return render(request, "task_index.html", {'tasks': models.Task.objects.all()})
    
def task_detail(request, task_id):
    task = models.Task.objects.get(id=task_id)
    return HttpResponse("Task ID: " + str(task_id) + "<br>" + task.title)