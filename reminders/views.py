from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from cep2015sem2.common.views import *
import datetime
from reminders import models, forms


class TaskIndexView(ListView):
    model = models.Task
    template_name = "task_index.html"


class TaskDetailView(DetailView):
    model = models.Task
    template_name = "task.html"
    context_object_name = 'task'


class TaskCreateView(BaseCreateView):
    model = models.Task
    form_class = forms.TaskForm
    item_type = "Task"


class TaskUpdateView(BaseUpdateView):
    model = models.Task
    form_class = forms.TaskForm


class TaskDeleteView(BaseDeleteView):
    model = models.Task
    success_url = reverse_lazy('task_index')
    form_class = forms.TagForm


class TagsCreateView(BaseCreateView):
    model = models.TaskTag
    form_class = forms.TagForm
    item_type = "Tag"


class TagsUpdateView(BaseUpdateView):
    model = models.TaskTag
    form_class = forms.TagForm


class TagsDeleteView(BaseDeleteView):
    model = models.TaskTag
    success_url = reverse_lazy('tags_index')
    form_class = forms.TagForm


class TagsIndexView(ListView):
    model = models.TaskTag
    template_name = "tag_index.html"


class TagsDetailView(DetailView):
    model = models.TaskTag
    template_name = "task_tag.html"
    context_object_name = "tag"
