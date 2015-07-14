from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
import datetime
from reminders import models


class TaskIndexView(ListView):
    model = models.Task
    template_name = "task_index.html"


class TaskDetailView(DetailView):
    model = models.Task
    template_name = "task.html"
    context_object_name = 'task'